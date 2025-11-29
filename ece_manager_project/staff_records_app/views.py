from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request,'staff_profile_page.html')
    

def staff_login(request):
    if request.method == 'POST':
        username  = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username , password=password).first()
        print(user)
        if user:
            print("Login Successful")
            return redirect('home')
    return render(request , 'login_page.html')