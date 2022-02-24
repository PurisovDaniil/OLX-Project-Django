from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name = 'register'),
    path('search/', views.search_function, name = 'search_url'),
    path('post_detail/', views.post_detail, name = 'post_detail_url'),
    path('categories/<slug:slug>', views.category_detail, name = 'category_detail_url'),
    path('profile/', views.profile, name = 'profile_url'),
    path('profile/save_bg/', views.save_bg, name = 'save_bg'),
    path('users/<str:username>', views.user_detail, name = 'user_detail'),
    path('authorisation/', views.authorisation, name = 'authorisation'),
    path('addpost/', views.addpost, name = 'addpost'),
    path('favorites/', views.favorites, name = 'favorites'),
    path('messages/', views.messages, name = 'messages'),
]