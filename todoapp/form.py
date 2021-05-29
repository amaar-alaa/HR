from django import forms
from .models import *

class RepoForm(forms.ModelForm):
    class Meta:
        model=Repo
        fields=['title','content']