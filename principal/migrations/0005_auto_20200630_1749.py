# Generated by Django 3.0.7 on 2020-06-30 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20200630_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institucion',
            name='escudo',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='perfil/', verbose_name='Escudo'),
        ),
    ]
