from .models import Messages
from django import forms

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields =['name','email','text']