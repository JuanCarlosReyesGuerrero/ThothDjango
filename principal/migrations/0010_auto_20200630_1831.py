# Generated by Django 3.0.7 on 2020-06-30 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0005_auto_20200630_1214'),
        ('principal', '0009_auto_20200630_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='departamento_expedicion_madre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departamento_expedicion_madre_set', to='configuracion.Departamento'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='departamento_expedicion_padre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracion.Departamento'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='departamento_expulsor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departamento_expulsor_set', to='configuracion.Departamento'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='departamento_residencia_madre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departamento_residencia_madre_set', to='configuracion.Departamento'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='fotografia',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='fotografia/', verbose_name='Fotografia'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='institucion_bienestar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='municipio_expedicion_madre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_expedicion_madre_set', to='configuracion.Municipio'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='municipio_expedicion_padre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_expedicion_padre_set', to='configuracion.Municipio'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='municipio_expulsor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_expulsor_set', to='configuracion.Municipio'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='municipio_residencia_madre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_residencia_madre_set', to='configuracion.Municipio'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='tipo_identificacion_madre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_identificacion_madre_set', to='configuracion.TipoIdentificacion'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='tipo_identificacion_padre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_identificacion_padre_set', to='configuracion.TipoIdentificacion'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ultimo_grado',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='zona_residencia_madre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zona_residencia_madre_set', to='configuracion.Zona'),
        ),
    ]
