from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('insertuser/',views.insertuser,name='insertuser')
   
]