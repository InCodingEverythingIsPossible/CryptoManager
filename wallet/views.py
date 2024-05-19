from django.shortcuts import render
# Create your views here.

#maybe tak
# class Wallet(render):
def wallet(request):
    return render(request, "home/base.html")


