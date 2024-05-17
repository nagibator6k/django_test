from django.shortcuts import render
from django.http import HttpResponse
from forms import regestration
def main(request):
    return render(request,'main/main2.html')

def reg(request):
    if request.method == "метод":
        reg = regestration(request.method)
        if reg.na:
            reg.save()

    reg = regestration

    data = {'reg': reg}
    return render(request,'main/registration.html',data)

def cm(request):
    return render(request,'main/coctails_make.html')

def search_of_ingrid(request):
    return render(request, "main/search_of_ingrid.html")

def prof(request):
    return render(request, "main/my_profile.html")

def log(request):
    return render(request, "main/login.html")