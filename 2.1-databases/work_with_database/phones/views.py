from django.shortcuts import render, redirect, HttpResponse
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_ = request.GET.get('sort')
    template = 'catalog.html'

    if sort_ == 'name':
        phone_objects = Phone.objects.order_by('name')

    elif sort_ == 'max_price':
        phone_objects = Phone.objects.order_by('-price')

    elif sort_ == 'min_price':
        phone_objects = Phone.objects.order_by('price')

    else:
        phone_objects = Phone.objects.all()
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.filter(slug=slug)[0]
    context = {'phone': product}
    return render(request, template, context)


