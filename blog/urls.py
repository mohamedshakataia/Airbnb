from django.urls import path
from .views import Aboutview , PostDetail


app_name='blog'

urlpatterns = [
    path('',Aboutview.as_view() ,name='blog'),
    path('<int:pk>',PostDetail.as_view() ,name='detail'),
]