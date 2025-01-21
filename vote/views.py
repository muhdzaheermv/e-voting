from django.shortcuts import render,redirect


def index(request):
    return render(request,"index.html")

def officer_home(request):
    return render(request,"officer_home.html")



