# Generated by Django 4.1.7 on 2023-07-09 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scd', '0011_rename_email_administrativo_correo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrativo',
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