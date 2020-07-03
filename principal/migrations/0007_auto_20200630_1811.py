# Generated by Django 3.0.7 on 2020-06-30 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0005_auto_20200630_1214'),
        ('principal', '0006_auto_20200630_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='barrio_madre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='barrio_padre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='celular_madre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='celular_padre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='certificado_expulsion',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='departamento_expedicion_madre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='departamento_expedicion_madre_set', to='configuracion.Departamento'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='departamento_expedicion_padre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='configuracion.Departamento'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='departamento_residencia_madre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='departamento_residencia_madre_set', to='configuracion.Departamento'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='departamento_residencia_padre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='departamento_residencia_padre_set', to='configuracion.Departamento'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='direccion_madre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email_madre',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email_padre',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='empresa_madre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='empresa_padre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='localidad_madre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='localidad_padre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='municipio_expedicion_madre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_expedicion_madre_set', to='configuracion.Municipio'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='municipio_expedicion_padre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_expedicion_padre_set', to='configuracion.Municipio'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='municipio_residencia_madre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_residencia_madre_set', to='configuracion.Municipio'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='municipio_residencia_padre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_residencia_padre_set', to='configuracion.Municipio'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ocupacion_madre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ocupacion_padre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='primer_apellido_madre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='primer_apellido_padre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='primer_nombre_madre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='primer_nombre_padre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_apellido_madre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_apellido_padre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_nombre_madre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_nombre_padre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='telefono_empresa_madre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='telefono_empresa_padre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='telefono_madre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='telefono_padre',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='tipo_identificacion_madre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_identificacion_madre_set', to='configuracion.TipoIdentificacion'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='tipo_identificacion_padre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_identificacion_padre_set', to='configuracion.TipoIdentificacion'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='zona_residencia_madre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='zona_residencia_madre_set', to='configuracion.Zona'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='zona_residencia_padre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='zona_residencia_padre_set', to='configuracion.Zona'),
        ),
    ]
