from django.http import HttpResponse
from django.shortcuts import render

from . models import Meet_the_Team


# Create your views here.
def home(request):
    obj = Meet_the_Team.objects.all()
    return render(request, "index.html", {'teams': obj})

# def about(request):
#     return render(request, "about.html")
#
# def contact(request):
#     return HttpResponse("Hello am contact")


