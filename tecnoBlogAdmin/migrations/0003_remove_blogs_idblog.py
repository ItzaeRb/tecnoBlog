# Generated by Django 4.1 on 2022-10-17 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tecnoBlogAdmin', '0002_alter_blogs_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='idBlog',
        ),
    ]