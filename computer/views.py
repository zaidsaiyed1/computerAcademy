from django.shortcuts import render,redirect
from django.http import *
from .models import user_details
# Create your views here.
def home(request):
     return render(request,'templates/home.html')

def success(request):
  return render(request, 'templates/success.html', {})
       
   
def insertuser(request):
    # if request.method == 'Post':
  vage = request.POST['uage'];
  vsex = request.POST['usex'];
  vcp = request.POST['ucp'];
  vtrestbps = request.POST['utrestbps'];
  vchol = request.POST['uchol'];
  vfbs = request.POST['ufbs'];
  vrestecg = request.POST['urestecg'];
  vthalach = request.POST['uthalach'];
  vexng = request.POST['uexng'];
  voldpeak = request.POST['uoldpeak'];
  vslp = request.POST['uslp'];
  vca = request.POST['uca'];
  vthal = request.POST['uthal'];
  vnum = request.POST['unum'];

  us = user_details(age=vage,sex=vsex,cp=vcp,trestbps=vtrestbps,chol=vchol,fbs=vfbs,restecg=vrestecg,thalach=vthalach,exng=vexng,oldpeak=voldpeak,slp=vslp,ca=vca,thal=vthal,num=vnum);
  us.save()     
  return render(request, 'templates/success.html', {})  
