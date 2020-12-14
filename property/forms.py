from django import forms
from .models import RoomBook

class RoomBookForm(forms.ModelForm):
    from_data = forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    to_data = forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    class Meta:
        model=RoomBook
        fields = '__all__'
        exclude = ['room',]