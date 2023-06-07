from django.shortcuts import render
from django.http import HttpResponse
from .models import product
def home(request):
    product = product.object.all()
  return render(request,'index1.html',{'product':product})

def contact(request):
    return HttpResponse("This is contact page")

def about(request):
    return HttpResponse("This is about page")

