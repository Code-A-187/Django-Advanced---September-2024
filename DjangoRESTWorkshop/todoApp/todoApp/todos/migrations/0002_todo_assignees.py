# Generated by Django 5.1.4 on 2024-12-19 10:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='assignees',
            field=models.ManyToManyField(blank=True, related_name='assigned_todos', to=settings.AUTH_USER_MODEL),
        ),
    ]