from django.urls import path
from . import views

app_name = 'godzilla'

urlpatterns = [
    path('', views.GodzillaView.as_view(), name='index'),
]
