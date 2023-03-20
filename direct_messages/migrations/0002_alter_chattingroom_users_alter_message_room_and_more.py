# Generated by Django 4.1.7 on 2023-03-20 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('direct_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chattingroom',
            name='users',
            field=models.ManyToManyField(related_name='chattingrooms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='direct_messages.chattingroom'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
