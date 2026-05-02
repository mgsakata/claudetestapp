from django.urls import path
from . import views

app_name = 'snowflakes'

urlpatterns = [
    path('', views.SnowflakesView.as_view(), name='index'),
]
