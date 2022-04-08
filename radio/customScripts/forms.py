from django.forms import ModelForm

from radio.models import messageRequest, audioRequest
from django import forms

class audioUploadForm(ModelForm):
    class Meta:
        model = audioRequest
        fields = ['name','artist','find_on','file']


class MessageUploadForm(ModelForm):
    class Meta:
        model = messageRequest

        fields = ['message','image']

        widgets = {
            "message": forms.Textarea(attrs={'class': 'textarea'}),
        }

