# Generated by Django 4.2.5 on 2023-09-15 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestorTareas', '0002_integrantes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='integrantes',
            name='email',
        ),
    ]