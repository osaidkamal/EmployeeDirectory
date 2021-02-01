from django.http import request
from .models import myuser
from .models import Detail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegForm, UserForm, logged
from .models import myuser
from django.shortcuts import (get_object_or_404,HttpResponseRedirect) 



@login_required(login_url="login")
def home(request):
    empl = Detail.objects.all()
    return render(request, 'index.html', {"employee": empl})


def registerhidden(request):
    context = {}
    if request.POST:
        form = RegForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get('password1')
            users = authenticate(email=email, password=raw_password)
            login(request, users)
            return redirect('login')
        else:
            context['registration_form'] = form

    else:
        form = RegForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)


@login_required(login_url="login")
def logoutas(request):
    logout(request)
    return redirect('/')


def loginas(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form = logged(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('/')
    else:
        form = logged()
    context['login_form'] = form
    return render(request, 'login.html', context)


@login_required(login_url="login")
def details(request, pk):
    users = Detail.objects.get(id=pk)
    if request.method == "POST":
            form = UserForm(request.POST, request.FILES,instance=users)
            if form.is_valid():
                form.save()
                return redirect("/show/"+str(pk))
    else:
            form = UserForm()
    if request.user == users.name:
        return render(request, "details.html", {'form': users})

    else:
        return redirect("/show/"+str(pk))


def show(request,pk):
    employees = Detail.objects.get(id=pk)
    return render(request, "show.html", {'employees': employees})

def update(request, pk): 
    obj=Detail.objects.get(id=pk)
    form=UserForm(instance=obj)
    if request.method=="POST":
        form=UserForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/show/"+str(pk))
    context={'form':form}
    return render(request,'details.html',context)