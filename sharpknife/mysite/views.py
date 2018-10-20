from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "mysite/index.html")


def ios(request):
    return render(request, "mysite/ios.html")


def update(request):
    return render(request, "mysite/update.html")
