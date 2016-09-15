from django import forms

class TreasureForm(forms.Form):
  name = forms.CharField(label='Name', max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control'}))
  value = forms.DecimalField(label='Value', max_digits=10, decimal_places=2,
    widget=forms.NumberInput(attrs={'class': 'form-control'}))
  material = forms.CharField(label='Material', max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control'}))
  location = forms.CharField(label='Location', max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control'}))
  img_url = forms.CharField(label='Image URL', max_length=255,
    widget=forms.TextInput(attrs={'class': 'form-control'}))
