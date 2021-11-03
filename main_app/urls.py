from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('registration/signup/', views.SignUp.as_view(), name="signup"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile/<int:pk>/', views.ProfileUpdate.as_view(), name="profile_update"),
    path('events/<int:pk>/', views.EventDetail.as_view(), name="event_detail"),
    path('events/new', views.CreateEvent.as_view(), name="create_event"),
    path('events/', views.EventList.as_view(), name="event_list"),
    path('events/<int:pk>/delete', views.EventDelete.as_view(), name='event_delete'),
    path('events/<int:pk>/update', views.EventUpdate.as_view(), name="event_update"),
]