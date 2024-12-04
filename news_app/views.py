from django.shortcuts import render, redirect
from .models import New, CategoryNews
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_page(request):
    try:
        if request.user.is_authenticated:
            news = New.objects.all()
            categories = CategoryNews.objects.all()
            context = {'news': news, 'categories': categories}
            return render(request, 'index.html', context)

    except:
        return redirect('about')
def about(request):
    try:
        if request.user.is_authenticated:
            redirect('home')
        return render(request, 'about.html')
    except:
        return render(request, 'about.html')

def category_page(request, pk):
    category = CategoryNews.objects.get(id=pk)
    news = New.objects.filter(new_category=category).all()
    context = {'news': news, 'category': category}

    return render(request, 'category_new.html', context)

def new_page(request,pk):
    new = New.object.get(id=pk)
    context = {'new': new}
    return render(request, 'new.html', context)