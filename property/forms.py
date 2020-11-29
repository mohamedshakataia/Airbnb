from django import forms
from .models import RoomBook

class RoomBookForm(forms.ModelForm):
    class Meta:
        model=RoomBook
        fields = '__all__'
        exclude = ['room',]