
from django.shortcuts import render, HttpResponse, redirect

def index(request):

    print "you made it this far"



    return render(request,"super/index.html")
