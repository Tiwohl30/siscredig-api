# Generated by Django 4.1.7 on 2023-03-14 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='carrera',
            field=models.ForeignKey(choices=[('Ingenieria de software', 'Ingenieria de software'), ('Ingeniería mecatronica', 'Ingeniería mecatronica'), ('Ingenieria en animacion y efectos visuales', 'Ingenieria en animacion y efectos visuales')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='scd.carrera'),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombre_carrera',
            field=models.CharField(choices=[('Ingenieria de software', 'Ingenieria de software'), ('Ingeniería mecatronica', 'Ingeniería mecatronica'), ('Ingenieria en animacion y efectos visuales', 'Ingenieria en animacion y efectos visuales')], max_length=120),
        ),
    ]