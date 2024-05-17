from django.shortcuts import render
from django.http import HttpResponse
def main(request):
    return render(request,'main/main2.html')

def about(request):
    return HttpResponse("<h4>about<h4>")

def reg(request):
    return render(request,'main/registration.html')
