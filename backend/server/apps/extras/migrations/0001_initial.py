# Generated by Django 4.2.4 on 2023-08-17 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.CharField(max_length=255, verbose_name='Tree class')),
                ('genus', models.CharField(max_length=255, verbose_name='Tree genus')),
                ('species', models.CharField(max_length=255, verbose_name='Tree species')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Sender's name")),
                ('email', models.EmailField(max_length=254, verbose_name='Your Email')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('message', models.TextField(max_length=255, verbose_name='Message')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date sent')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Notification title')),
                ('status', models.CharField(choices=[('unread', 'unread'), ('read', 'read')], default='unread', max_length=20, verbose_name='Status')),
                ('time_sent', models.CharField(max_length=150, verbose_name='Time sent')),
            ],
        ),
        migrations.CreateModel(
            name='TreeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(max_length=255, verbose_name='Tree genus')),
                ('more_info', models.TextField(blank=True, default='No additional information given', max_length=255, verbose_name='Additional information')),
                ('files', models.FileField(blank=True, upload_to='', verbose_name='Evidence')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]