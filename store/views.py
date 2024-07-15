from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.views.generic import ListView, CreateView
from .forms import ProductForm
from rest_framework import viewsets
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'price']
    template_name = 'store/product_form.html'
    success_url = '/store/products/'

def home(request):
    return render(request, 'store/home.html')

def test(request):
    return render(request, 'store/test.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'store/product_confirm_delete.html', {'product': product})

def products(request):
    return render(request, 'store/products.html')
