from django import forms
from .models import Treasure

class TreasureForm(forms.ModelForm):
  class Meta:
    model = Treasure
    fields = ['name', 'value', 'location', 'material', 'image']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'value': forms.NumberInput(attrs={'class': 'form-control'}),
      'location': forms.TextInput(attrs={'class': 'form-control'}),
      'material': forms.TextInput(attrs={'class': 'form-control'}),
      'image': forms.FileInput(attrs={'class': 'form-control'})
    }

class LoginForm(forms.Form):
  username = forms.CharField(label='User Name', max_length=64,
    widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control'}))