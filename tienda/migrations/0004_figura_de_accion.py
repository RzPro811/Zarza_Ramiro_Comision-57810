# Generated by Django 5.0.6 on 2024-07-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_cartas_en_stock_cartas_precio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Figura_de_Accion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('figura', models.CharField(max_length=50)),
                ('origen', models.CharField(max_length=50)),
                ('fabricante', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('en_stock', models.BooleanField()),
                ('disponibles', models.IntegerField()),
            ],
        ),
    ]