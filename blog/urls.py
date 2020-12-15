from django.urls import path
from .views import postview , PostDetail


app_name='blog'

urlpatterns = [
    path('',postview.as_view() ,name='blog'),
    path('<int:pk>',PostDetail.as_view() ,name='detail'),
]