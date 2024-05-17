from django.shortcuts import render
from django.http import HttpResponse
def main(request):
    return render(request,'main/main2.html')

def reg(request):
    return render(request,'main/registration.html')

def cm(request):
    return render(request,'main/coctails_make.html')

def search_of_ingrid(request):
    return render(request, "main/search_of_ingrid.html")