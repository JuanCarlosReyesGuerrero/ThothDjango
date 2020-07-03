# Generated by Django 3.0.7 on 2020-06-04 03:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_auto_20200603_2217'),
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('codigoMEN', models.CharField(max_length=20)),
                ('numero_documento', models.CharField(max_length=20)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(max_length=20)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateTimeField(blank=True)),
                ('email', models.CharField(max_length=50)),
                ('fotografia', models.ImageField(upload_to='')),
                ('direccion', models.CharField(max_length=100)),
                ('localidad', models.CharField(max_length=100)),
                ('barrio', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
                ('numero_sisben', models.CharField(max_length=30)),
                ('fecha_expulsion', models.DateTimeField(blank=True, null=True)),
                ('certificado_expulsion', models.CharField(max_length=20)),
                ('fecha_certificado_expulsion', models.DateTimeField(blank=True, null=True)),
                ('proviene_sector_privado', models.BooleanField(default=False)),
                ('proviene_otro_municipio', models.BooleanField(default=False)),
                ('institucion_bienestar', models.CharField(max_length=100)),
                ('numero_documento_madre', models.CharField(max_length=20)),
                ('primer_apellido_madre', models.CharField(max_length=20)),
                ('segundo_apellido_madre', models.CharField(max_length=20)),
                ('primer_nombre_madre', models.CharField(max_length=20)),
                ('segundo_nombre_madre', models.CharField(max_length=20)),
                ('email_madre', models.CharField(max_length=50)),
                ('direccion_madre', models.CharField(max_length=100)),
                ('barrio_madre', models.CharField(max_length=100)),
                ('localidad_madre', models.CharField(max_length=100)),
                ('telefono_madre', models.CharField(max_length=20)),
                ('celular_madre', models.CharField(max_length=20)),
                ('ocupacion_madre', models.CharField(max_length=100)),
                ('empresa_madre', models.CharField(max_length=100)),
                ('telefono_empresa_madre', models.CharField(max_length=20)),
                ('numero_documento_padre', models.CharField(max_length=20)),
                ('primer_apellido_padre', models.CharField(max_length=20)),
                ('segundo_apellido_padre', models.CharField(max_length=20)),
                ('primer_nombre_padre', models.CharField(max_length=20)),
                ('segundo_nombre_padre', models.CharField(max_length=20)),
                ('email_padre', models.CharField(max_length=50)),
                ('direccion_padre', models.CharField(max_length=100)),
                ('barrio_padre', models.CharField(max_length=100)),
                ('localidad_padre', models.CharField(max_length=100)),
                ('telefono_padre', models.CharField(max_length=20)),
                ('celular_padre', models.CharField(max_length=20)),
                ('ocupacion_padre', models.CharField(max_length=100)),
                ('empresa_padre', models.CharField(max_length=100)),
                ('telefono_empresa_padre', models.CharField(max_length=20)),
                ('numero_documento_acudiente', models.CharField(max_length=20)),
                ('primer_apellido_acudiente', models.CharField(max_length=20)),
                ('segundo_apellido_acudiente', models.CharField(max_length=20)),
                ('primer_nombre_acudiente', models.CharField(max_length=20)),
                ('segundo_nombre_acudiente', models.CharField(max_length=20)),
                ('email_acudiente', models.CharField(max_length=50)),
                ('direccion_acudiente', models.CharField(max_length=100)),
                ('barrio_acudiente', models.CharField(max_length=100)),
                ('localidad_acudiente', models.CharField(max_length=100)),
                ('telefono_acudiente', models.CharField(max_length=20)),
                ('celular_acudiente', models.CharField(max_length=20)),
                ('ocupacion_acudiente', models.CharField(max_length=100)),
                ('empresa_acudiente', models.CharField(max_length=100)),
                ('telefono_empresa_acudiente', models.CharField(max_length=20)),
                ('colegio_ultimo_curso', models.CharField(max_length=100)),
                ('direccion_colegio_ultimo_curso', models.CharField(max_length=100)),
                ('telefono_colegio_ultimo_curso', models.CharField(max_length=20)),
                ('ultimo_grado', models.CharField(max_length=20)),
                ('anio', models.CharField(max_length=4)),
                ('motivo_retiro_ultimo', models.CharField(max_length=255)),
                ('observaciones', models.TextField()),
                ('usuario_estudiante', models.CharField(max_length=20)),
                ('clave_acceso', models.CharField(max_length=20)),
                ('seleccione_madre', models.BooleanField(default=False)),
                ('seleccione_padre', models.BooleanField(default=False)),
                ('seleccione_acudiente', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('ars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Ars')),
                ('capacidad_excepcional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.CapacidadExcepcional')),
                ('departamento_expedicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento_expedicion_set', to='configuracion.Departamento')),
                ('departamento_expedicion_acudiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento_expedicion_acudiente_set', to='configuracion.Departamento')),
                ('departamento_expedicion_madre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento_expedicion_madre_set', to='configuracion.Departamento')),
                ('departamento_expedicion_padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Departamento')),
                ('departamento_expulsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento_expulsor_set', to='configuracion.Departamento')),
                ('departamento_nacimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento_nacimiento_set', to='configuracion.Departamento')),
                ('departamento_residencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento_residencia_set', to='configuracion.Departamento')),
                ('departamento_residencia_acudiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento_residencia_acudiente_set', to='configuracion.Departamento')),
                ('departamento_residencia_madre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento_residencia_madre_set', to='configuracion.Departamento')),
                ('departamento_residencia_padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento_residencia_padre_set', to='configuracion.Departamento')),
                ('eps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Eps')),
                ('estrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Estrato')),
                ('etnia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Etnia')),
                ('factor_rh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.FactorRh')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Genero')),
                ('genero_acudiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genero_acudiente_set', to='configuracion.Genero')),
                ('grupo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.GrupoUsuario')),
                ('municipio_expedicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_expedicion_set', to='configuracion.Municipio')),
                ('municipio_expedicion_acudiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_expedicion_acudiente_set', to='configuracion.Municipio')),
                ('municipio_expedicion_madre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_expedicion_madre_set', to='configuracion.Municipio')),
                ('municipio_expedicion_padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_expedicion_padre_set', to='configuracion.Municipio')),
                ('municipio_expulsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_expulsor_set', to='configuracion.Municipio')),
                ('municipio_nacimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_nacimiento_set', to='configuracion.Municipio')),
                ('municipio_residencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Municipio')),
                ('municipio_residencia_acudiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_residencia_acudiente_set', to='configuracion.Municipio')),
                ('municipio_residencia_madre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_residencia_madre_set', to='configuracion.Municipio')),
                ('municipio_residencia_padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_residencia_padre_set', to='configuracion.Municipio')),
                ('parentesco_acudiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Parentesco')),
                ('poblacion_victima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.PoblacionVictimaConflicto')),
                ('resguardo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Resguardo')),
                ('sisben', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Sisben')),
                ('tipo_discapacidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.TipoDiscapacidad')),
                ('tipo_identificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.TipoIdentificacion')),
                ('tipo_identificacion_acudiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_identificacion_acudiente_set', to='configuracion.TipoIdentificacion')),
                ('tipo_identificacion_madre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_identificacion_madre_set', to='configuracion.TipoIdentificacion')),
                ('tipo_identificacion_padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_identificacion_padre_set', to='configuracion.TipoIdentificacion')),
                ('zona_residencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zona_residencia_set', to='configuracion.Zona')),
                ('zona_residencia_acudiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zona_residencia_acudiente_set', to='configuracion.Zona')),
                ('zona_residencia_madre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zona_residencia_madre_set', to='configuracion.Zona')),
                ('zona_residencia_padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zona_residencia_padre_set', to='configuracion.Zona')),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('codigo_dane', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=20)),
                ('nombre_rector', models.CharField(max_length=100)),
                ('numero_sedes', models.IntegerField()),
                ('subsidio', models.BooleanField(default=False)),
                ('decreto_creacion', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=100)),
                ('secretaria', models.CharField(max_length=100)),
                ('aprobacion', models.CharField(max_length=30)),
                ('lema', models.CharField(max_length=255)),
                ('escudo', models.ImageField(upload_to='')),
                ('barrio', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('sitio_web', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('numero_liciencia', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('asociacion_privada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.AsociacionPrivada')),
                ('calendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Calendario')),
                ('capacidad_excepcional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.CapacidadExcepcional')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Departamento')),
                ('etnia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Etnia')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genero_set', to='configuracion.Genero')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Idioma')),
                ('metodologia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Metodologia')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Municipio')),
            ],
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='Active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='Codigo',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='escalanacional',
            old_name='Active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='escalanacional',
            old_name='Codigo',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='escalanacional',
            old_name='CriterioEvaluacion',
            new_name='criterio_evaluacion',
        ),
        migrations.RenameField(
            model_name='escalanacional',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=12)),
                ('codigo_dane_nuevo', models.CharField(max_length=12)),
                ('codigo_dane_antiguo', models.CharField(max_length=12)),
                ('codigo_consecutivo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('barrio', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('jornada_completa', models.BooleanField(default=False)),
                ('jornada_manana', models.BooleanField(default=False)),
                ('jornada_tarde', models.BooleanField(default=False)),
                ('jornada_noche', models.BooleanField(default=False)),
                ('jornada_fin_semana', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(blank=True)),
                ('director', models.CharField(max_length=30)),
                ('secretaria', models.CharField(max_length=30)),
                ('escala_valoracion_nacional', models.BooleanField(default=False)),
                ('rango_numerico', models.BooleanField(default=False)),
                ('numero_inicial', models.IntegerField()),
                ('numero_final', models.IntegerField()),
                ('valoracion_letras', models.BooleanField(default=False)),
                ('juicios', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Departamento')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Especialidad')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Institucion')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Municipio')),
                ('tipo_novedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.TipoNovedad')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Zona')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('numero_documento', models.CharField(max_length=20)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(max_length=20)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('escalafon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Escalafon')),
                ('profesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Profesion')),
                ('tipo_identificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.TipoIdentificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Nucleo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('nombre_director', models.CharField(max_length=30)),
                ('telefono_director', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Departamento')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad_matricula', models.CharField(max_length=255)),
                ('numero_matricula', models.CharField(max_length=255)),
                ('numero_folio', models.CharField(max_length=255)),
                ('fecha_matricula', models.DateTimeField(blank=True)),
                ('anio_matricula', models.DateTimeField(blank=True)),
                ('estado_matricula', models.IntegerField()),
                ('repitente', models.BooleanField(default=False)),
                ('observaciones', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Estudiante')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Grado')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Grupo')),
                ('jornada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Jornada')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Sede')),
                ('tipo_caracter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.TipoCaracter')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=255)),
                ('intensidad_horaria', models.IntegerField()),
                ('orden', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Grado')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Grupo')),
                ('jornada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Jornada')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Juicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Grado')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Grupo')),
                ('jornada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Jornada')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Materia')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Periodo')),
            ],
        ),
        migrations.AddField(
            model_name='institucion',
            name='nucleo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Nucleo'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='prestador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Prestador'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='propiedad_juridica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.PropiedadJuridica'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='regimen_costo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.RegimenCosto'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='resguardo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Resguardo'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='tarifa_anual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.TarifaAnual'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='tipo_discapacidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.TipoDiscapacidad'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='tipo_novedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.TipoNovedad'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='tipo_sector_educacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.TipoSectorEducacion'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Zona'),
        ),
        migrations.CreateModel(
            name='Equivalencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('rango_numerico_menor', models.DecimalField(decimal_places=1, max_digits=18)),
                ('rango_numerico_mayor', models.DecimalField(decimal_places=1, max_digits=18)),
                ('rango_simbolo_menor', models.CharField(max_length=2)),
                ('rango_simbolo_mayor', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('escala_nacional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.EscalaNacional')),
                ('valor_letra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.ValoracionLetra')),
            ],
        ),
    ]