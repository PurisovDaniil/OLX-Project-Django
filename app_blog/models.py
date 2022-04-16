from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    background = models.ImageField('Фон профиля', blank=True, null=True, upload_to='users/bg')
    avatar = models.ImageField('Аватар', blank=True, null=True, upload_to='users/avatars')
    phone = models.CharField('Номер пользователя', max_length=13)
    birth_date = models.DateField('Дата рождения', null=True)

    class Meta:
        verbose_name = 'Дополнительное поле пользователя'
        verbose_name_plural = 'Дополнительные поля пользователя'

    def __str__(self):
        return self.user.username

class Image(models.Model):
    image = models.ImageField('Картинка', upload_to = 'image/')
    title = models.CharField('Заголовок', max_length = 100)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField('Заголовок', max_length = 255)
    slug = models.SlugField('Ссылка', unique = True) 
    image = models.ImageField('Картинка', blank = True, null = True)
    
    class Meta():
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def get_link(self):
        return reverse('category_detail_url', kwargs = {'slug': self.slug})
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='favorite_products')
    price = models.IntegerField(default=False)
    description = models.CharField(max_length=455)
    image = models.ImageField(null=True, blank=True)
    sity_title = models.CharField(max_length=255)
    usernumber = models.IntegerField(default=False)
    username = models.CharField(max_length=15)

class Favourite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)