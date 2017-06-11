from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from site0.models import Product, Shop, Categorie

def home(request):
    products = Product.objects.all()
    return render(request, 'site0/home.html', {'last_products': products})

def lire(request, id):
    try:
        article = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404

    return render(request, 'site0/lire.html', {'article': article})

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé")

def date_actuelle(request):
    return render(request, 'site0/date.html', {'date':datetime.now()})

def addition(request, nbr1, nbr2):
    total = int(nbr1)+int(nbr2)
    return render(request, 'site0/addition.html', locals())

def mypage(request):
    return reverse(request, 'site0/mypage.html')
