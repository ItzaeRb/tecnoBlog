# Generated by Django 4.1 on 2022-10-19 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tecnoBlog', '0004_merge_0002_delete_usuarios_0003_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blogs',
        ),
    ]