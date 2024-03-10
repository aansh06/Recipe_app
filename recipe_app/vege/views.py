from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
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





