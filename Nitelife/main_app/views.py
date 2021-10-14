from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

# Create your views here.


from django.views import View
from django.views.generic.base import TemplateView
from .models import (Event, User)
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.urls import reverse
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

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
          
