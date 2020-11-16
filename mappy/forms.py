from django import forms
from mappy.models import Coord

class CoordForm (forms.ModelForm):
    address = forms.CharField(required = False, widget=forms.TextInput(attrs={'placeholder':'es. Via Roma 17 Udine'}))

    class Meta:
        model = Coord
        fields = ['lat','lng']
        widgets = {
            'lat': forms.HiddenInput(),
            'lng': forms.HiddenInput(),
        }
