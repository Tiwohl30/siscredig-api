# Generated by Django 4.1.7 on 2023-07-09 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scd', '0010_remove_alumno_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrativo',
            old_name='email',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='docente',
            old_name='email',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='otros',
            old_name='email',
            new_name='correo',
        ),
    ]
