from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import Post, Category, Image, Profile, Comment

# Create your views here.

def index(request):
    news = Post.objects.filter(publish = 1).order_by('-views')[:3]
    categories = Category.objects.all()[:12]
    context = {'news': news, 'categories': categories}
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
    posts = Post.objects.filter(Q(title__icontains = query))
    context = {'query': query, 'posts': posts}
    return render(request, 'app_blog/search.html', context)

def save_bg(request):
    if request.method == 'POST':
        form = UserBG('request.POST, request.FILES')
        if form.is_valid():
            form.save(request.user)
    return redirect('index')

def user_detail(request, username):
    user = User.objects.get(username=username)
    views = user.views_set.order_by('-date')
    comments = user.comment_set.order_by('-date')
    context = {'user':user, 'views':views, 'comments':comments}
    return render(request, 'blog/user_detail.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug__exact = slug)
    post.views += 1
    post.save()
    return render(request, 'app_blog/post_detail.html', {'post':post})


def comment(request, slug):
    post = Post.objects.get
    if request.method == 'POST':
        post.comment_set.create(user = request.user, text = request.POST.get('text'))
        return redirect(reverse('post_detail_url', kwargs = {'slug':post.slug}))
    return redirect(reverse('post_detail_url', kwargs = {'slug':post.slug}))

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

def add_post(request):
    return render(request, 'app_blog/add_post.html')