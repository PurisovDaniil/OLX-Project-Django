from django.shortcuts import render, redirect, reverse
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import Category, Product, Favourite
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.db.models.deletion import ProtectedError
from django.core.mail import send_mail

# Create your views here.

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'categories': categories, 'page_obj' : page_obj}
    return render(request, 'app_blog/index.html', context)

def favourites(request):
    if request.user.is_authenticated:
        product = Favourite.objects.filter(user=request.user)
        return render(request, 'app_blog/favorites.html', {'product':product})
    return redirect('authorisation')

def add_to_favourite(request, product_id):
    product = Product.objects.get(id = product_id)
    if request.user.is_authenticated:
        if not request.user.favourite_set.filter(product = product).exists():
            item = Favourite()
            item.product = product
            item.user = request.user
            item.save()
        return redirect('index')
    return redirect('authorisation')

def delete_favourite(request, item_id):
    item = Favourite.objects.get(id=item_id)
    if request.user.is_authenticated:
        item.delete()
        return redirect('favourites')
    return redirect('authorisation')

def mobileapps(request):
    return render(request, 'app_blog/mobileapps.html')

def mainhelp(request):
    return render(request, 'app_blog/help.html')

def payments(request):
    return render(request, 'app_blog/payments.html')

def reklama(request):
    return render(request, 'app_blog/reklama.html')

def rules(request):
    return render(request, 'app_blog/rules.html')

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
    products = Product.objects.filter(Q(title__icontains = query))
    context = {'query': query, 'products': products}
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

def authorisation(request):
    return render(request, 'app_blog/authorisation.html')

def addpost(request):
    category = Category.objects.all()
    return render(request, 'app_blog/add_post.html', {'category':category})

def create(request):
    if request.method == 'POST':
        product = Product()
        product.title = request.POST.get('title')
        product.category = Category.objects.get(id=request.POST.get('category'))
        product.description = request.POST.get('description')
        if request.FILES.get('image', False) != False:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            product.image = filename
        product.sity_title = request.POST.get('sity_title')
        product.price = request.POST.get('price')
        product.usernumber = request.POST.get('usernumber')
        product.username = request.POST.get('username')
        product.save()
    return redirect('index')
    
def update(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        if request.FILES.get('image', False) != False:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            product.image = filename
        product.sity_title = request.POST.get('sity_title')
        product.usernumber = request.POST.get('usernumber')
        product.save()
        return redirect('index')
    return render(request, 'app_blog/update.html', {'product':product})

def delete(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        try:
            product.delete()
            return redirect(reverse('index'))
        except ProtectedError:
            return HttpResponse('не нихуя')
    return render(request, 'app_blog/delete.html', {'product':product})

def messages_ads(request):
    return render(request, 'app_blog/messages_ads.html')

def developers(request):
    return render(request, 'app_blog/developers.html')

def error(request):
    return render(request, 'app_blog/error.html')

def careers(request):
    return render(request, 'app_blog/cariera-index.html')

def hybrid(request):
    return render(request, 'app_blog/careers-hybrid.html')

def story(request):
    return render(request, 'app_blog/careers-story.html')

def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.title = request

def contact_us(request):
    if request.method == 'POST':
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        context = {'message_name':message_name, 'message_email':message_email, 'message':message}
        send_mail(message_name, message, message_email, ['daniilpurisov393@gmail.com'])
        return render(request, 'app_blog/contact_us.html', context)
    else:
        return render(request, 'app_blog/contact_us.html')