from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import Movieform
# Create your views here.
def index(request):
    Movie = movie.objects.all()
    context={
        'movie_list':Movie
    }
    return render(request,'index.html',context)

def details(request,movie_id):
    Movie= movie.objects.get(id=movie_id)
    return render(request,"details.html",{'Movie':Movie})

def add(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        decs = request.POST.get('decs',)
        year = request.POST.get('year', )
        img= request.FILES['img']
        Movie=movie(name=name,decs=decs,year=year,img=img)
        Movie.save()
    return render(request,'add.html')

def update(request,id):
    Movie=movie.objects.get(id=id)
    forms=Movieform(request.POST or None,request.FILES,instance=Movie)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'forms':forms,'movie':movie})

def delete(request,id):
    if request.method == "POST":
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')

