# Generated by Django 5.0.6 on 2024-07-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_remove_peluches_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='peluches',
            name='foto',
            field=models.ImageField(default='default.png', upload_to='Peluches/'),
        ),
    ]