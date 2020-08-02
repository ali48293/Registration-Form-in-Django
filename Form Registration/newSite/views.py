from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,"navbar.html")


def register(request):
    
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        
        if pass1 == pass2 :
            if User.objects.filter(username=username).exists():
                
                messages.info(request,"username already in use!")
                return redirect("register")
            
            else:
                user = User.objects.create_user(username = username, email=email,password=pass1,first_name=first_name,last_name=last_name)
                user.save()
                return redirect("login")
        else:
            messages.info(request,"password is not matching!")
            return redirect("register")
        
    # else:
    #     messages.info(request,"Invalid Credentiala!")
    #     return redirect("register")
    
    return render(request,"register.html")
    
    
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]
        user = auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credentials!")
            return redirect("login")
    return render(request,"login.html")




def logout(request):
    auth.logout(request)
    return redirect("/")