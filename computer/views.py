from django.shortcuts import render,redirect
from django.http import request
import csv
import pandas as pd
from .models import user_details, user_data1
# Create your views here.
def index(request):
     return render(request,'templates/index.html',{})
def home(request):
     return render(request,'templates/home.html',{})
def contactus(request):
     return render(request,'templates/contact-us.html',{})
def about(request):
     return render(request,'templates/about.html',{})
def features(request):
     return render(request,'templates/features.html',{})
def result(request):
  return render(request, 'templates/result.html', {})
def result1(request):
  return render(request, 'templates/result1.html', {})
#this will read the csv file
def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data  
#Section will check the data with the csv file data  to predict heart disease
def calculate_heart_disease(request,data, user_data):
  
  heart_damage1 = False
  heart_damage2 = False
  heart_damage3 = False
  heart_damage4 = False
  for row in data[1:]:
        icity = str(row[0])
        istate = str(row[1])
        icountry = str(row[2])
        iage = int(row[3])
        isex = str(row[4])
        icp = str(row[5])
        idiabi = str(row[6])
        isob = str(row[7])
        ibps = str(row[8])
        ifati = str(row[9])
        inov = str(row[10])
        iioh = str(row[11])
        ies = str(row[12])
        ihhd = str(row[13])
        
        if icity == user_data['ucity'] and istate == user_data['ustate']:
           if (icountry == user_data['ucountry'] and iage == user_data['uage'] and isex == user_data['usex']  and icp == user_data['ucp'] and idiabi == user_data['udiabi'] and isob == user_data['usob'] and ibps == user_data['ubps'] and ifati ==user_data['ufati'] and inov ==user_data['unov'] and iioh ==user_data['uioh'] and ies == user_data['ues']and ihhd == user_data['uhhd']):
               heart_damage1 = True
               break
           elif(icountry == user_data['ucountry'] and iage == user_data['uage'] and isex ==user_data['usex']  and icp == user_data['ucp'] and idiabi == user_data['udiabi'] and isob == user_data['usob'] or ibps == user_data['ubps']and ifati ==user_data['ufati'] and inov ==user_data['unov']  and iioh ==user_data['uioh'] and ies ==user_data['ues'] and ihhd == user_data['uhhd']):
                heart_damage2 = True
                break
           elif(icountry == user_data['ucountry'] and iage == user_data['uage'] and isex ==user_data['usex']  and icp == user_data['ucp'] or idiabi == user_data['udiabi'] and isob == user_data['usob'] and ibps ==user_data['ubps']  and ifati ==user_data['ufati'] or inov == user_data['unov'] and iioh ==user_data['uioh'] and ies == user_data['ues']and ihhd == user_data['uhhd']):
              heart_damage3 = True
              break
           elif(icountry ==user_data['ucountry']  or iage == user_data['uage'] or isex ==user_data['usex']  or icp == user_data['ucp'] or idiabi == user_data['udiabi'] or isob == user_data['usob'] or ibps ==user_data['ubps']  or ifati ==user_data['ufati'] or inov ==user_data['unov']  or iioh ==user_data['uioh'] or ies ==user_data['ues'] or ihhd == user_data['uhhd']):
              heart_damage4 = True
              break
 
  if heart_damage1 :
        return render(request, 'templates/result1.html',{'heart_damage1':heart_damage1})
  elif heart_damage2:
        return render(request, 'templates/result1.html',{'heart_damage2':heart_damage2})
  elif heart_damage3:
        return render(request, 'templates/result1.html',{'heart_damage3':heart_damage3})
  elif heart_damage4:
        return render(request, 'templates/result1.html',{'heart_damage4':heart_damage4})

    # No match found
  #return render(request, 'templates/result.html')

  #this section i sused to store the user value in the databse 

def insertuser(request):
#   if request.method == 'Post':
  vcity = request.POST['ucity'];
  vstate = request.POST['ustate']; 
  vcountry = request.POST['ucountry'];
  vage = request.POST['uage'];
  vsex = request.POST['usex'];
  vcp = request.POST['ucp'];
  vdiabi = request.POST['udiabi'];
  vsob = request.POST['usob'];
  vbps = request.POST['ubps'];
  vfati = request.POST['ufati'];
  vnov = request.POST['unov'];
  vioh = request.POST['uioh'];
  ves = request.POST['ues'];
  vhhd = request.POST['uhhd'];
  us = user_details(city = vcity,state = vstate,country = vcountry,age=vage, sex=vsex, cp=vcp, diabi=vdiabi,fati=vfati, ioh=vioh, es=ves,nov=vnov, bps=vbps, sob=vsob, hhd=vhhd);
  us.save(); 
  #if request.method == 'POST':
  user_data = {
            'ucity' : str(request.POST['ucity']),
            'ustate' : str(request.POST['ustate']),            
            'ucountry': str(request.POST['ucountry']),
            'uage': int(request.POST['uage']),
            'usex': str(request.POST['usex']),
            'ucp': str(request.POST['ucp']),
            'udiabi': str(request.POST['udiabi']),
            'usob': str(request.POST['usob']),
            'ubps': str(request.POST['ubps']),
            'ufati': str(request.POST['ufati']),
            'unov': str(request.POST['unov']),
            'uioh': str(request.POST['uioh']),
            'ues': str(request.POST['ues']),
            'uhhd': str(request.POST['uhhd']),
        }
  predict =calculate_heart_disease(request,data, user_data)
  return predict
 #return 
# this fubction is to store the user feedback in the database
def user_data(request):
  #if request.method == 'POST':
    udname =  request.POST['ucname'];
    udage = request.POST['ucage'];
    udsex = request.POST['ucsex'];
    udcountry = request.POST['uccountry'];
    udemail = request.POST['ucemail'];
    udfeedb = request.POST['ucfeedback'];
    u = user_data1(uname=udname,ucountry=udcountry,uage=udage,usex=udsex,uemail=udemail,ufeedb=udfeedb);
    u.save();
    return render(request,'templates/result.html', {})



file_path = 'D:\\pythonpro\\computerAcademy\\Dataset\\new_data.csv'  # csv file path
data = read_csv_file(file_path)

