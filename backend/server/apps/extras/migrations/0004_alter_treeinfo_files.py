# Generated by Django 4.2.4 on 2023-10-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0003_notifications_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treeinfo',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Evidence'),
        ),
    ]
