from django.shortcuts import render ,reverse
from . import models
from django.views.generic import DetailView
from django_filters.views import FilterView
from .fillter import propertyFilter
from django.views.generic.edit import FormMixin
from .forms import RoomBookForm
# Create your views here.



class RoomList(FilterView):
    model=models.Room
    filterset_class = propertyFilter
    template_name= 'property/room_list.html'


class RoomDetail(FormMixin,DetailView):
    model=models.Room
    form_class = RoomBookForm
    success_url = '/rooms/' 


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()