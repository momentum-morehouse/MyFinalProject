from django import forms
from .models import Profile

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'location',
            'position',
            'image_url',
            'interest',
        ]
      

        widgets = {
        'date_released': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }