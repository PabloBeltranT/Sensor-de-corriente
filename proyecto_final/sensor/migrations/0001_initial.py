# Generated by Django 3.2.2 on 2021-05-14 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_de_consumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=50)),
                ('hora', models.CharField(max_length=50)),
                ('corrinete_consimuda_en_directa', models.CharField(max_length=50)),
                ('potencia_consumida_en_directa', models.CharField(max_length=50)),
                ('timepo_de_consumo_en_red_comercial', models.CharField(max_length=50)),
            ],
        ),
    ]
