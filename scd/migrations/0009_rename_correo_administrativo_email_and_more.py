# Generated by Django 4.1.7 on 2023-07-09 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scd', '0008_administrativo_credencial_activa_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrativo',
            old_name='correo',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='correo',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='docente',
            old_name='correo',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='otros',
            old_name='correo',
            new_name='email',
        ),
    ]
