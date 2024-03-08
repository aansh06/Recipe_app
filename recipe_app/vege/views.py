from django.shortcuts import render , redirect
from .models import *
# Create your views here.


def home(request):
    queryset = Receipe.objects.all()
    context = {'recipes':queryset}
    return render(request,'home.html',context)




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