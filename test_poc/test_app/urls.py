from django.urls import path
from . import views
urlpatterns = [
              path('', views.home),
              path('welcome', views.welcome),
              path('insert', views.insertdata),
              path('display', views.display_details),
              ]