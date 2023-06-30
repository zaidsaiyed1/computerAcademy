from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('insertuser/',views.insertuser,name='insertuser'),
    path('success/',views.success,name='success'),
     path('success/',views.result,name='result'),
]