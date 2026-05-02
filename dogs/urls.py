from django.urls import path
from . import views

app_name = 'dogs'

urlpatterns = [
    path('', views.DogsView.as_view(), name='index'),
]
