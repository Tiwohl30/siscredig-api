# Generated by Django 4.1.7 on 2023-07-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scd', '0002_alter_alumno_carrera_alter_carrera_nombre_carrera'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('idCarrera', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_carrera', models.CharField(choices=[('Ingenieria de software', 'Ingenieria de software'), ('Ingeniería mecatronica', 'Ingeniería mecatronica'), ('Ingenieria en animacion y efectos visuales', 'Ingenieria en animacion y efectos visuales')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='alumno',
            name='carrera',
            field=models.CharField(choices=[('Ingenieria de software', 'Ingenieria de software'), ('Ingeniería mecatronica', 'Ingeniería mecatronica'), ('Ingenieria en animacion y efectos visuales', 'Ingenieria en animacion y efectos visuales')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Carrera',
        ),
    ]
