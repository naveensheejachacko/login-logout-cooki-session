
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache 
from django.http import HttpResponseRedirect
#
from django.contrib import messages

# Create your views here.

def user_login(request):
    if 'username' in request.session:
        if 'username' in request.COOKIES:
            if request.session['username']==request.COOKIES['username']:
                return redirect(home)
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        response=redirect('home')
        if user is not None:
            response.set_cookie('username',username)
            request.session['username']=username
            return response

        else:
            return render(request,'login.html',{'error_msg':"Invalid Credentials!!!!"})
    return render(request,'login.html')


def home(request):
    if 'username' in request.session and 'username' in request.COOKIES:
        return render(request,'home.html')
    return redirect(user_login)



def user_logout(request):
    response=HttpResponseRedirect(reverse('login'))
    request.session.flush()
    response.delete_cookie('username')
    return HttpResponseRedirect(reverse('login'))