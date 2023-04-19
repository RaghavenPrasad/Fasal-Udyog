from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import stock_center

# Create your views here.
def home(request):
    name = "FasalUdyog"
    return render(request, "home.html", {
        "name": name
    })

def registerfarmer(request):
    submitted = False
    if request.method == "POST":
        form = farmerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/register_farmer?submitted=True")
    else:
        form = farmerForm()
        if "submitted" in request.GET:
            submitted = True
    return render(request, "registerfarmer.html", {
        "form": farmerForm(),
        "submitted": submitted,
    })

def checkstock(request):
    error = False
    if request.method == "POST":
        item_id = request.POST["item_id"]
        stock = stock_center.objects.filter(item_id=item_id)
        if item_id == "":
            return render(request, "checkstock.html", {
                "stock": stock_center.objects.all()
            })
        if not stock:
            error = True
        return render(request, "checkstock.html", {
            "stock": stock,
            "error": error,
        })
    return render(request, "checkstock.html", {
        "stock": stock_center.objects.all()
    })

def order(request):
    submitted = False
    if request.method == "POST":
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/order?submitted=True")
    else:
        form = orderForm()
        if "submitted" in request.GET:
            submitted = True
    return render(request, "order.html", {
        "form": orderForm(),
        "submitted": submitted,
    })

def about(request):
    return render(request, "aboutus.html")