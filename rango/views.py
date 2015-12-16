from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.forms import CategoryForm


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return hello(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    return render(request, 'rango/add_category.html', {'form': form})


def about(request):
    return render(request, 'rango/about.html')


def hello(request):
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)
