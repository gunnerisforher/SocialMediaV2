# Generated by Django 4.2 on 2023-05-04 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created']},
        ),
    ]
