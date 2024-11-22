from django.shortcuts import render
from .models import New, CategoryNews

# Create your views here.
def home_page(request):
    news = New.objects.all()
    categories = CategoryNews.objects.all()
    context = {'news': news, 'categories': categories}
    return render(request, 'home.html', context)

def category_page(request, pk):
    category = CategoryNews.objects.get(id=pk)
    news = New.objects.filter(new_category=category)
    context = {'news': news}
    return render(request, 'category.html', context)

def new_page(request,pk):
    new = New.object.get(id=pk)
    context = {'new': new}
    return render (request, 'new.html', context)