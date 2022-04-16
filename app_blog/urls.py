from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name = 'register'),
    path('search/', views.search_function, name = 'search_url'),
    path('post_detail/<int:id>/', views.post_detail, name = 'post_detail_url'),
    path('categories/<slug:slug>', views.category_detail, name = 'category_detail_url'),
    path('profile/save_bg/', views.save_bg, name = 'save_bg'),
    path('authorisation/', views.authorisation, name = 'authorisation'),
    path('addpost/', views.addpost, name = 'addpost'),
    path('favourites/', views.favourites, name = 'favourites'),
    path('myaccount/answers/', views.messages, name = 'messages'),
    path('favourite/add/<int:product_id>/', views.add_to_favourite, name = 'add_favourite'),
    path('favourite/delete/<int:item_id>/', views.delete_favourite, name = 'delete_favourite'),
    path('myaccount/ads/', views.messages_ads, name = 'messages_ads'),
    path('create', views.create, name = 'create'),
    path('mobileapps/', views.mobileapps, name = 'mobileapps'),
    path('developers', views.developers, name = 'developers'),
    path('help.olx.uz/pravila-publikacii', views.error, name = 'error'),
    path('careers.olx.group', views.careers, name = 'careers'),
    path('careers.olx.group/hybrid-work-at-olx/', views.hybrid, name = 'hybrid'),
    path('careers.olx.group/story', views.story, name = 'story'),
    path('delete_product/<int:id>', views.delete, name = 'delete'),
    path('update/<int:id>', views.update, name = 'update'),
    path('olx/help', views.mainhelp, name = 'main_help'),
    path('olx/payments', views.payments, name = 'payments'),
]