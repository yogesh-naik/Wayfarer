from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView
from .models import (Event, User, Profile)
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.urls import reverse
from django.contrib import messages
from .forms import EventForm, ProfileForm, form_validation_error

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
        context["events"] = Event.objects.all()
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
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)

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

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('profile')


    
# def CreateEvent(request):
#     form = EventForm()
    
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('/')
    

#     context = {'form':form}
#     return render(request,"createevent.html",context)

class CreateEvent(CreateView):
    model = Event
    fields = ['title', 'location','bio', 'image','guest']
    template_name = "create_event.html"


    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(CreateEvent, self).form_valid(form)
    

    def get_success_url(self):
        print(self.kwargs)
        # return reverse('event_detail', kwargs={'pk': self.object.pk})
        return reverse("eventlist")

class EventUpdate(UpdateView):
    model = Eventfields = ['title', 'location','bio', 'image','guest']
    template_name = "event_update.html"
    success_url = "/events/"

