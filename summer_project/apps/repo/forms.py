from django import forms
from django .forms import widgets
from .models import Inspiration


class Contribute_Form(forms.ModelForm):
    class Meta:
        model = Inspiration
        fields = ['inspire_content']