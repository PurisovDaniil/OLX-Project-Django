from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import Category, Image, Profile, Product
from django.shortcuts import render, redirect
from .models import Product
from django.core.paginator import Paginator
from django.utils import timezone

# Create your views here.

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'categories': categories, 'page_obj' : page_obj}
    return render(request, 'app_blog/index.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'app_blog/register.html', {"form":form})

def search_function(request):
    query = request.GET.get('search_input')
    posts = Product.objects.filter(Q(title__icontains = query))
    context = {'query': query, 'posts': posts}
    return render(request, 'app_blog/search.html', context)

def save_bg(request):
    if request.method == 'POST':
        form = UserBG('request.POST, request.FILES')
        if form.is_valid():
            form.save(request.user)
    return redirect('index')

def post_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'app_blog/post_detail.html', {'product' : product})

def category_detail(request, slug):
    category = Category.objects.get(slug__exact = slug)
    return render(request, 'app_blog/category_detail.html', {'category':category})

def profile(request):
    if not request.user.is_authenticated:
        return redirect('index')
    views = request.user.views_set.order_by('-date')
    comments = request.user.comment_set.order_by('-date')
    formBG = UserBG()
    context = {'views':views, 'comments':comments, 'formBG':formBG}
    return render(request, 'blog/profile.html', context)

def authorisation(request):
    return render(request, 'app_blog/authorisation.html')

def addpost(request):
    return render(request, 'app_blog/add_post.html')

def create(request):
    if request.method == 'POST':
        product = Product()
        product.title = request.POST.get('title')
        product.date = request.POST.get('date')
        product.description = request.POST.get('description')
        product.image = request.POST.get('image')
        product.sity_title = request.POST.get('sity_title')
        product.price = request.POST.get('price')
        product.save()
    return redirect('index')

def favorites(request):
    return render(request, 'app_blog/favorites.html')

def messages(request):
    return render(request, 'app_blog/messages.html')

def favorites_search(request):
    return render(request, 'app_blog/favorites_search.html')

def favorites_lastseen(request):
    return render(request, 'app_blog/favorites_lastseen.html')

def messages_ads(request):
    return render(request, 'app_blog/messages_ads.html')

def messages_settings(request):
    return render(request, 'app_blog/messages_settings.html')

def messages_wallet(request):
    return render(request, 'app_blog/messages_wallet.html')

def main_help(request):
    return render(request, 'app_blog/help.html')

def more_myprofile(request):
    return render(request, 'app_blog/more_myprofile.html')

def more_information(request):
    return render(request, 'app_blog/more_information.html')

def my_profile_registration(request):
    return render(request, 'app_blog/my_profile_registration.html')

def profile_settings_all(request):
    return render(request, 'app_blog/profile_settings_all.html')

def mobile_registration(request):
    return render(request, 'app_blog/my_profile_registration_mobile.html')

def verification(request):
    return render(request, 'app_blog/my_profile_verification.html')

def developers(request):
    return render(request, 'app_blog/developers.html')

def mobileapps(request):
    return render(request, 'app_blog/mobileapps.html')

def payments(request):
    return render(request, 'app_blog/payments.html')

def reklama(request):
    return render(request, 'app_blog/reklama.html')

def rules(request):
    return render(request, 'app_blog/rules.html')

def security(request):
    return render(request, 'app_blog/security.html')

def error(request):
    return render(request, 'app_blog/error.html')

def how_buy(request):
    return render(request, 'app_blog/how_to_buy.html')

def how_sell(request):
    return render(request, 'app_blog/how_to_sell.html')

def careers(request):
    return render(request, 'app_blog/cariera-index.html')

def hybrid(request):
    return render(request, 'app_blog/careers-hybrid.html')