from django.urls import path
from . import views

app_name = 'biosphere'

urlpatterns = [
    path('', views.BiosphereView.as_view(), name='index'),
]
