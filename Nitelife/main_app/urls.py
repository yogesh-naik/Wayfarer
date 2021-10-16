from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('registration/signup/', views.SignUp.as_view(), name="signup"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('events/<int:pk>/', views.EventDetail.as_view(), name="event_detail"),
    path('events/new', views.CreateEvent.as_view(), name="createevent"),
    path('events/', views.EventList.as_view(), name="eventlist"),
    path('events/<int:pk>/delete', views.EventDelete.as_view(), name='event_delete')
    path('events/<int:pk>/update', views.EventUpdate.as_view(), name="event_update"),
]