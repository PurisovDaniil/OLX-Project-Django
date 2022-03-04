# Generated by Django 3.2.9 on 2022-03-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=False)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(max_length=455)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
