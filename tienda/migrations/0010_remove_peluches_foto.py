# Generated by Django 5.0.6 on 2024-07-18 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_alter_peluches_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peluches',
            name='foto',
        ),
    ]