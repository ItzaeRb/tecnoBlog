# Generated by Django 4.1 on 2022-10-19 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnoBlogAdmin', '0003_remove_blogs_idblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinatario', models.CharField(max_length=30)),
                ('contenido', models.CharField(max_length=500)),
                ('remitente', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='blogs',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]