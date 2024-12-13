from django.shortcuts import render

# Create your views here.
def landingpage(request):
    return render(request,'landingpage.html')

def loginpage(request):
    return render(request,'loginpage.html')

def registration(request):
    return render(request,'registration.html')

def admindashboard(request):
    return render(request,'admindashboard.html')