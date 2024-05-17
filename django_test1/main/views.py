from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'main/main2.html')

def about(request):
    return HttpResponse("<h4>about<h4>")
