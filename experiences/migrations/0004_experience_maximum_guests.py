# Generated by Django 4.1.7 on 2023-04-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0003_alter_experience_category_alter_experience_host_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='maximum_guests',
            field=models.IntegerField(default=0),
        ),
    ]
