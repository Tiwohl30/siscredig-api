# Generated by Django 4.1.7 on 2023-07-09 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scd', '0009_rename_correo_administrativo_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='email',
        ),
    ]
