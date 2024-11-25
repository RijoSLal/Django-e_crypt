import re
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
import hashlib
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
# Create your views here.
@never_cache
def login(request):
   
        if request.method =='POST':
            username_login=request.POST.get("username")
            password_login=request.POST.get("password")

            
            
            user = authenticate(username=username_login,password=password_login)
            
            if user is not None:
                auth_login(request,user)
                
                return redirect('admin_page') if user.is_superuser else redirect('app_page')
          
            else:
                messages.error(request, "Incorrect username or password")
                return redirect('login_page')
        
        return render(request,'log_in.html')

@never_cache
def signup(request):
    if request.user.is_authenticated:
       return redirect("login_page")
    else:
        if request.POST:
            usernames=request.POST.get("username")
            emails=request.POST.get("email")
            password_one=request.POST.get("password_one")
            password_two=request.POST.get("password_two")
            
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            username_regex = r'^[a-zA-Z0-9_]{3,20}$'
            password_regex = r'^.{4,}$'


            available=User.objects.filter(email=emails).exists()
            if re.fullmatch(email_regex,emails):
                
                if available:      
                    messages.error(request,"Email already exists")
                elif password_one!=password_two:
                    messages.error(request,'Passwords do not match')
                elif User.objects.filter(username=usernames).exists():
                    messages.error(request,"Username already exists")
                elif re.fullmatch(username_regex, usernames) is None:
                    messages.error(request, "Username is invalid")
                elif re.fullmatch(password_regex, password_one) is None:
                    messages.error(request, "Password is too short")
                else:
                
                    user=User.objects.create_user(username=usernames ,email=emails,password=password_one)
                    user.save()
                    return redirect('login_page')
                    
                
                        
            else:
                messages.error(request,"Invalid email format")
                

        return render(request,'sign_in.html')
@never_cache
def log_out(request):
    logout(request)
    messages.success(request,"Logging out")
    return redirect("login_page")

@never_cache
@login_required
def home(request):
    if request.user.is_authenticated:
        if request.POST:
            username=request.POST.get("username")
            context={}
            created=hashlib.sha256(username.encode()).hexdigest()[0:10]
            context['created']=created
            return render(request,'generate.html',context)
                
        return render(request,'generate.html')
    else:
        return redirect('login_page')

@never_cache
def admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        all_users=User.objects.all()
        return render(request,'admin.html',{'content':all_users})
        
    else:
        return redirect('login_page')




def delete(request,pk):
    instance=User.objects.get(pk=pk)
    instance.delete()
    all_users=User.objects.all()
    return render(request,'admin.html',{'content':all_users})

def edit(request,pk):
    instance=User.objects.get(pk=pk)
    if request.POST:
        usernames=request.POST.get("username")
        emails=request.POST.get("email")
        password_one=request.POST.get("password_one")
        password_two=request.POST.get("password_two")
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        
        if re.fullmatch(regex,emails):
            
            if password_one!=password_two:
                messages.error(request,'Passwords do not match')
            elif check_password(password_one,instance.password)==False:
                messages.error(request,'Passwords incorrect')
            
            else:
                instance.username=usernames
                instance.email=emails
                instance.save()
                return redirect('admin_page')         
        else:
            messages.success(request,"Invalid email format")
            

    return render(request,'sign_in.html',{"instance":instance})

@never_cache
def search(request):
    if request.method == 'POST': 
        searched = request.POST.get('searches', '')  

        venue = User.objects.filter(username__icontains=searched)
        print(venue)
        print(searched)
        return render(request, 'search.html', {"searched": searched, "venue": venue})
    else:
        return render(request, 'search.html')