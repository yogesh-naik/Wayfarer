from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('registation/signup/', views.SignUp.as_view(), name="signup"),
]