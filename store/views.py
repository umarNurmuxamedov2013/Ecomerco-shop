from django.contrib.auth.forms import UserCreationForm
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404


def index(request):
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    data = {
        "all_products": all_products,
        "all_categories": all_categories
    }

    return render(request, "store/store.html", data)


@login_required(login_url='store')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # Kategoriyani topamiz
    products = Product.objects.filter(product_ctg=category)  # Shu kategoriyaga tegishli productlarni olamiz

    context = {
        'category': category,
        'products': products
    }
    return render(request, 'store/category_products.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store')  # Kirgandan keyin qayerga yo‘naltirish kerak bo‘lsa, shu joyni o'zgartiring
        else:
            messages.error(request, "Login yoki parol xato!")

    return render(request, 'store/login.html')


def log_out(request):
    logout(request)
    return redirect('login')


# Ro'yxatdan o'tish
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = form.save()
            login(request, user)
            messages.success(request, f"Hisobingiz muvaffaqiyatli yaratildi, {username}!")
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'store/register.html', {'form': form})


def custom_404(request):
    return render(request, '404.html', status=404)


handler_404 = custom_404


def detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    data = {
        "product": product,
    }
    return render(request, 'store/product-info.html', data)


def list_category(request, slug_category=None):
    category = get_object_or_404(request, Category, slug=slug_category)
    product = Product.objects.filter(category=category)
    data = {
        "category": category,
        "product": product,
    }
    return render(request, 'store/list-category.html', data)
