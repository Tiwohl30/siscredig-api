# Generated by Django 4.1.7 on 2023-07-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scd', '0003_carreras_alter_alumno_carrera_delete_carrera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='fotografia',
            field=models.ImageField(null=True, upload_to='fotografias_alumnos/'),
        ),
    ]
