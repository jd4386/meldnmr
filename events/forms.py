from django import forms
from django.forms import ModelForm
from .models import RequestModel

class RequestModelForm(ModelForm):
    class Meta:
        model = RequestModel
        fields = ['name', 'email', 'file']