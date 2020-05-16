# Generated by Django 3.0.5 on 2020-05-15 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_auto_20200514_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.OneToOneField(default='userprofile/user.jpeg', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]