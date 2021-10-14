from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('registration/signup/', views.SignUp.as_view(), name="signup"),
]