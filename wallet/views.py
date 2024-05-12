from django.shortcuts import render
# Create your views here.


def wallet(request):
    return render(request, "home/base.html")


