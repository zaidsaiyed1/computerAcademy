from django.shortcuts import render,redirect
from django.http import request
import csv
import pandas as pd
from .models import user_details
# Create your views here.
def home(request):
     return render(request,'templates/home.html',)

def success(request):
  return render(request, 'templates/success.html', {})

def result(request):
    return render(request,'templates/result.html', {})
#this will read the csv file
def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data  
#Section will check the data with the csv file data    
def calculate_heart_disease(request,data, user_data):
    heart_damage = False
    for row in data[1:]:
        iage = int(row[0])
        isex = int(row[1])
        icp = int(row[2])
        itrestbps = int(row[3])
        ichol = int(row[4])
        ifbs = int(row[5])
        irestecg = int(row[6])
        ithalach = int(row[7])
        iexng = int(row[8])
        ioldpeak = float(row[9])
        islp = int(row[10])
        ica = int(row[11])
        ithal = int(row[12])
        inum = int(row[13])

        if (
            iage == user_data['uage'] and
            isex == user_data['usex'] and
            icp == user_data['ucp'] and
            itrestbps == user_data['utrestbps'] and
            ichol == user_data['uchol'] and
            ifbs == user_data['ufbs'] and
            irestecg == user_data['urestecg'] and
            ithalach == user_data['uthalach'] and
            iexng == user_data['uexng'] and
            ioldpeak == user_data['uoldpeak'] and
            islp == user_data['uslp'] and
            ica >= user_data['uca'] and
            ithal == user_data['uthal'] and
            inum == user_data['unum']
        ):
            heart_damage = True
            break

    if heart_damage==True:
     return render(request, 'templates/success.html', {'heart_damage': heart_damage})
    else:
     return render(request,'templates/result.html')
  #this section i sused to store the user value in the databse 
def insertuser(request):
#   if request.method == 'Post':
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
  us = user_details(age=vage, sex=vsex, cp=vcp, trestbps=vtrestbps, chol=vchol, fbs=vfbs, restecg=vrestecg,thalach=vthalach, exng=vexng, oldpeak=voldpeak, slp=vslp, ca=vca, thal=vthal, num=vnum);
  us.save() 
  #if request.method == 'POST':
  user_data = {
            'uage': int(request.POST['uage']),
            'usex': int(request.POST['usex']),
            'ucp': int(request.POST['ucp']),
            'utrestbps': int(request.POST['utrestbps']),
            'uchol': int(request.POST['uchol']),
            'ufbs': int(request.POST['ufbs']),
            'urestecg': int(request.POST['urestecg']),
            'uthalach': int(request.POST['uthalach']),
            'uexng': int(request.POST['uexng']),
            'uoldpeak': float(request.POST['uoldpeak']),
            'uslp': int(request.POST['uslp']),
            'uca': int(request.POST['uca']),
            'uthal': int(request.POST['uthal']),
            'unum': int(request.POST['unum'])
        }
  predict =calculate_heart_disease(request,data, user_data)
  return predict
 #return 

#def predict_heart_damage(request):
#  pass
   # h =  
   # return h

file_path = 'D:\\Nichetech\\Dataset\\Heart_data.csv'  # csv file path
data = read_csv_file(file_path)
