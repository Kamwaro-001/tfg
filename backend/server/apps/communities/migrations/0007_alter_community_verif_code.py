# Generated by Django 4.2.4 on 2023-08-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0006_alter_community_verif_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='verif_code',
            field=models.CharField(default='G0ZJNTB5', max_length=9, unique=True, verbose_name='Verification code'),
        ),
    ]
