# Generated by Django 5.0.6 on 2024-07-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juego', models.CharField(max_length=50)),
                ('adultos', models.BooleanField()),
                ('cantCartas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Juegos_de_Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juego', models.CharField(max_length=50)),
                ('adultos', models.BooleanField()),
                ('piezas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Peluches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('en_stock', models.BooleanField()),
            ],
        ),
    ]
