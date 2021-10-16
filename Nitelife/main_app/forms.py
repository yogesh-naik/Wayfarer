from django import forms
from .models import Event, Profile
from django.forms import ModelForm

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['creator', 'title', 'location','bio', 'image','guest']