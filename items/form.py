from django import forms
from .models import *


class ProductForm (forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'What is your name',
            'image':'Photo'
            
        }


class UnitForm (forms.ModelForm):

    class Meta:
        model = Unit
        fields = '__all__'


class DepartForm (forms.ModelForm):

    class Meta:
        model = Depart
        fields = '__all__'


class CurnForm(forms.ModelForm):
    class Meta:
        model=Curn
        fields = '__all__'
        labels = {
            'value':'1 $ equales'
            
        }

