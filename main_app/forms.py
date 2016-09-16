from django import forms
from .models import Treasure

class TreasureForm(forms.ModelForm):
  class Meta:
    model = Treasure
    fields = ['name', 'value', 'location', 'material', 'img_url']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'value': forms.NumberInput(attrs={'class': 'form-control'}),
      'location': forms.TextInput(attrs={'class': 'form-control'}),
      'material': forms.TextInput(attrs={'class': 'form-control'}),
      'img_url': forms.TextInput(attrs={'class': 'form-control'})
    }