from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
# Create your views here.


# ........HOME PAGE

def home(request):
    queryset = Receipe.objects.all()
    if 'query' in request.GET:
        queryset=queryset.filter(receipe_name__icontains = request.GET['query'])
        if not queryset:
            return redirect('/')


    
    return render(request,'home.html',context= {'recipes':queryset})


# ..........add recipe page

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name= data.get('receipe_name')
        receipe_description= data.get('receipe_description')
        receipe_image= request.FILES.get('receipe_image')

        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        Receipe.objects.create(
             receipe_name= receipe_name,
            receipe_description= receipe_description,
            receipe_image= receipe_image
        )

        return redirect('/home/recipe')
    

    
    return render(request,'receipes.html')


# .......update recipe page

def update_recipe(request,id):
    
    queryset = Receipe.objects.get(id=id)
    
    if request.method == "POST":
        data = request.POST
        receipe_name= data.get('receipe_name')
        receipe_description= data.get('receipe_description')
        receipe_image= request.FILES.get('receipe_image')
        
        queryset.receipe_name= receipe_name
        queryset.receipe_description= receipe_description
        if receipe_image:
            queryset.receipe_image= receipe_image
        
        queryset.save()
        return redirect('/')
    return render(request,'update_recipe.html',context={'recipe':queryset})


# .......delete a recipe 

def delete_recipe(request,id):

    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/")


# .......login page
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username or password')
            return redirect('/home/login')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('/home/login')
        else:
            login(request, user)
            
            return redirect('/')

    return render(request, 'login.html')




# .......register page
def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # if username already exists
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('/home/register')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)  # to save password in encrypted format
        user.save()
        messages.info(request, 'Account created successfully')

        return redirect('/home/register')

    return render(request, 'register.html')



# ....... logout
def logout_page(request):
    logout(request)
    return redirect('/')
