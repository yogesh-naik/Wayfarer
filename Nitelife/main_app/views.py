
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView 
from .models import (Event, User, Profile)
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.urls import reverse
from django.contrib import messages
from .forms import form_validation_error, ProfileUpdateForm, UserCreationForm, UserUpdateForm

# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'home.html'


class EventList(TemplateView):
    template_name = 'events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        location = self.request.GET.get("location")
    
        if location != None:
            context["events"] = Event.objects.filter(location__icontains=location)
            context['header'] = location
        else:
            context["events"] = Event.objects.all()

        cities = []
        for e in context['events']:
            if e.location in cities:
                None
            else:
                cities.append(e.location)

        
        context['cities'] = cities

        return context

    
class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/profile')
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)
    
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile}
        print(self.profile)
        return render(request, 'profile.html', {'profile': self.profile})



@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'email','bio', 'city', 'avatar']
    template_name = "profile_update.html"
    success_url = '/profile/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateEvent(CreateView):
    model = Event
    fields = ['title', 'location','bio', 'image', 'video']
    template_name = "create_event.html"

    def upload_video(request):
    
        if request.method == 'POST': 
        
            video = request.POST['video']
        
            content = Event(video=video)
            content.save()
            return redirect('events')
    
        return render(request,'upload.html')

    def display(request):
        video = Event.objects.all()
        context ={
            'video':video,
        }
        return render(request,'events.html',context)

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.creator = profile
        return super(CreateEvent, self).form_valid(form)
    
    def get_success_url(self):
        print(self.kwargs)
        # return reverse('event_detail', kwargs={'pk': self.object.pk})
        return reverse("event_list")


@method_decorator(login_required(login_url='login'), name='dispatch')
class EventDetail(DetailView):
    model = Event
    template_name = "event_detail.html"

@method_decorator(login_required(login_url='login'), name='dispatch')
class EventDelete(DeleteView):
    model = Event
    template_name = "event_delete.html"
    success_url = "/events/"

@method_decorator(login_required(login_url='login'), name='dispatch')
class EventUpdate(UpdateView):
    model = Event
    fields = ['title', 'location','bio', 'image', 'video']
    template_name = "event_update.html"
    
    def get_success_url(self):
        print(self.kwargs)
        # return reverse('event_detail', kwargs={'pk': self.object.pk})
        return reverse("event_detail", kwargs={'pk': self.object.pk})
