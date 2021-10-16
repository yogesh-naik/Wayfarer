from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('registration/signup/', views.SignUp.as_view(), name="signup"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('events/new', views.CreateEvent.as_view(), name="createevent"),
    path('events/', views.EventList.as_view(), name="eventlist"),
]