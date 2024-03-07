from django.shortcuts import render
def homePage(request):
    return render(request, "index.html")
def loginpage(request):
    return render(request,"login.html")
def aboutpage(request):
    return render(request,"about.html")
def registrationPage(request):
    return render(request,"register.html")