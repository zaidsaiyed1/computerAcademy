from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('home/',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('features/',views.features, name='features'),
    path('contact-us/',views.contactus, name='contact-us'),
    path('insertuser/',views.insertuser,name='insertuser'),
    path('user_data/',views.user_data,name='user_data'),
    path('result1/',views.result1,name='result1'),
    path('result/',views.result,name='result'),
]