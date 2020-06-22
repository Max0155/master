from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import ProductForm


class HomeIndex(ListView):
    model = Product
    context_object_name = 'products' #По дефолту object_list
    template_name = 'shop/index.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Product.objects.filter(is_published=True).select_related('category')# Отображает только опубликованные данные.

# def index(request):
#     products = Product.objects.order_by('-created_at')  # order_by сортировщик так сказать
#     context = {
#         'products': products,
#         'title': 'Список товаров',
#     }
#     return render(request, 'shop/index.html', context=context)

class ProductByCategory(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/category.html'
    allow_empty = False #Запрет показа пустых списков

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')# Отображает только опубликованные данные.

# def get_category(request, category_id):
#     products = Product.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'shop/category.html',
#                   {'products': products, 'category': category})


class ViewProduct(DetailView):
    model = Product
    template_name = 'shop/product_view.html'
    context_object_name = 'product_item'


# def view_product(request, shop_id):
#     #product_item = Product.objects.get(pk=shop_id)
#     product_item = get_object_or_404(Product, pk=shop_id)
#     return render(request, 'shop/product_view.html', {"product_item": product_item})



class CreateProduct(CreateView):
    form_class = ProductForm
    template_name = 'shop/add_product.html'
    queryset = Product.objects.select_related('title')

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#             return redirect(product)
#     else:
#         form = ProductForm()
#     return render(request, 'shop/add_product.html', {'form': form})

