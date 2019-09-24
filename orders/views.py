from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    return render(request, "orders/index.html")


def menu(request):
    context = {
        "subs": Sub.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "dinnerplates": DinnerPlatters.objects.all()
    }
    return render(request, "orders/menu.html", context)
