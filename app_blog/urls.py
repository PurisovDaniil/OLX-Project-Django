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
    path('help.olx.uz/как_заказать_пакет?', views.packet, name = 'packet'),
    path('help.olx.uz', views.main_help, name = 'main_help'),
    path('help.olx.uz/приложение_6', views.app_6, name = 'app_6'),
    path('help.olx.uz/что_такое_пакет?', views.what_packet, name = 'what_packet'),
    path('help.olx.uz/какой_срок_действия_пакета?', views.validity_packet, name = 'validity_packet'),
    path('help.olx.uz/что-такое-дополнительное-размещение?', views.accommodation, name = 'accommodation'),
    path('help.olx.uz/profile_settings/ADs', views.profile_settings_ad, name = 'profile_settings_ad'),
    path('help.olx.uz/profile_settings/All', views.profile_settings_all, name = 'profile_settings_all'),
    path('help.olx.uz/profile_settings/change_pw_mobile', views.profile_settings_ch_pw_mobile, name = 'profile_settings_ch_pw_mobile'),
    path('help.olx.uz/profile_settings/change', views.profile_settings_change, name = 'profile_settings_change'),
    path('help.olx.uz/profile_settings/ID', views.profile_settings_id, name = 'profile_settings_id'),
    path('help.olx.uz/profile_settings/messages', views.profile_settings_messages, name = 'profile_settings_messages'),
]