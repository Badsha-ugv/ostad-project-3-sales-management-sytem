from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required 
import random 
from django.core.mail import send_mail 



from .models import UserProfile, LoginOTP
from .forms import LoginForm , RegisterForm


def login_view(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return redirect('index:home')
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = form.get_user()
            if user is not None and user.is_active:
                new_otp = ''.join([str(random.randint(0,6)) for _ in range(6)])
                print(new_otp)
                otp, created = LoginOTP.objects.get_or_create(user=user)
                otp.otp = new_otp
                otp.save()
                request.session['otp_user'] = user.username

                send_mail(
                    'Login OTP',
                    f'Your login OTP is: {new_otp}',
                    'admin_mail@example.com',
                    ['usermail@gmail.com'],)
                
                return redirect('account:otp_view')
            else:
                form.add_error(None, 'Invalid username or password.')
        else:
            return render(request, 'registration/login.html', {'form': form})
    return render(request, 'registration/login.html', {'form': form})


def otp_view(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        username = request.session['otp_user']
        if not username:
            return redirect('account:login')
        user = User.objects.get(username=username)
        otp_obj = LoginOTP.objects.get(user=user)
        if otp_obj.otp == otp:
            user.is_active = True
            user.save()
            login(request, user)
            otp_obj.otp = ''
            otp_obj.save()
            del request.session['otp_user'] 
            return redirect('index:home')
        else:
            return render(request, 'registration/otp_view.html', {'error': 'Invalid OTP'})
    return render(request, 'registration/otp_view.html')


def logout_view(request):
    logout(request)
    return redirect('account:login')


def register_view(request):
    form = RegisterForm()
    if request.user.is_authenticated:
        return redirect('index:home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True # future changes for email confirmation
            user.save()
            profile = UserProfile.objects.create(user=user)

            return redirect('account:login')
        else:
            return render(request, 'registration/register.html', {'form': form})
        
    return render(request, 'registration/register.html',{'form': form})


