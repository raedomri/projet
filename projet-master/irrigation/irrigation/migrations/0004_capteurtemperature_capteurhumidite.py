# Generated by Django 4.2.1 on 2023-06-21 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('irrigation', '0003_plant_nbre_valve'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapteurTemperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.DecimalField(decimal_places=2, max_digits=5)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irrigation.zone')),
            ],
        ),
        migrations.CreateModel(
            name='CapteurHumidite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.DecimalField(decimal_places=2, max_digits=5)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irrigation.zone')),
            ],
        ),
    ]