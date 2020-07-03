# Generated by Django 3.0.7 on 2020-06-03 21:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=6)),
                ('Nombre', models.CharField(max_length=255)),
                ('Active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=255)),
                ('Active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AsociacionPrivada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=2)),
                ('Nombre', models.CharField(max_length=255)),
                ('Active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=2)),
                ('Nombre', models.CharField(max_length=255)),
                ('Active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CapacidadExcepcional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=2)),
                ('Nombre', models.CharField(max_length=255)),
                ('Active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=2)),
                ('Nombre', models.CharField(max_length=255)),
                ('Active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=4)),
                ('Nombre', models.CharField(max_length=255)),
                ('Active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
