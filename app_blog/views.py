from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import Post, Category, Image, Profile, Comment

# Create your views here.

def index(request):
    news = Post.objects.all
    categories = Category.objects.all()
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


def post_detail(request):
    return render(request, 'app_blog/post_detail.html')


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

def addpost(request):
    return render(request, 'app_blog/add_post.html')

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

def packet(request):
    return render(request, 'app_blog/packet.html')

def app_6(request):
    return render(request, 'app_blog/app_6.html')

def what_packet(request):
    return render(request, 'app_blog/what_packet.html')

def validity_packet(request):
    return render(request, 'app_blog/validity_packet.html')

def accommodation(request):
    return render(request, 'app_blog/accommodation.html')

def main_help(request):
    return render(request, 'app_blog/help.html')

def profile_settings_ad(request):
    return render(request, 'app_blog/profile_settings_ad.html')

def profile_settings_all(request):
    return render(request, 'app_blog/profile_settings_all.html')

def profile_settings_ch_pw_mobile(request):
    return render(request, 'app_blog/profile_settings_ch_pw_mobile.html')

def profile_settings_change_pw(request):
    return render(request, 'app_blog/profile_settings_change_pw.html')

def profile_settings_change(request):
    return render(request, 'app_blog/profile_settings_change.html')

def profile_settings_id(request):
    return render(request, 'app_blog/profile_settings_id.html')

def profile_settings_messages(request):
    return render(request, 'app_blog/profile_settings_messages.html')

def profile_settings_resume(request):
    return render(request, 'app_blog/profile_settings_resume.html')

def profile_settings_uvedom(request):
    return render(request, 'app_blog/profile_settings_uvedom.html')