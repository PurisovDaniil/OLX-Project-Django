from unicodedata import name
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
    path('myaccount/answers/', views.messages, name = 'messages'),
    path('favorites/search', views.favorites_search, name = 'favorites_search'),
    path('favorites/lastseen', views.favorites_lastseen, name = 'favorites_lastseen'),
    path('myaccount/wallet/', views.messages_wallet, name = 'messages_wallet'),
    path('myaccount/settings/', views.messages_settings, name = 'messages_settings'),
    path('myaccount/ads/', views.messages_ads, name = 'messages_ads'),
    path('help.olx.uz', views.main_help, name = 'main_help'),
    path('help.olx.uz/my_profile/', views.more_myprofile, name = 'more_myprofile'),
    path('help.olx.uz/information', views.more_information, name = 'more_information'),
    path('help.olx.uz/my_profile/registration', views.my_profile_registration, name = 'myprofileregistration'),
    path('help.olx.uz/profile_settings', views.profile_settings_all, name = 'profilesettingsall'),
    path('help.olx.uz/my_profile/registration_mobile', views.mobile_registration, name = 'mobileregistration'),
    path('help.ox.uz/my_profile/verification', views.verification, name = 'verification'),
    path('create', views.create, name = 'create'),
]