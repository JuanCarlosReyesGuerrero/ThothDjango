from django.contrib.auth.models import Group
from django.db import models
from django.utils import timezone

from configuracion.models import Departamento, Etnia, Genero, FactorRh, GrupoUsuario, Calendario, Idioma, \
    Jornada, Municipio, Metodologia, Profesion, Escalafon, Especialidad, TipoIdentificacion, Zona, \
    Sisben, PoblacionVictimaConflicto, Resguardo, TipoDiscapacidad, Parentesco, TipoSectorEducacion, PropiedadJuridica, \
    TipoNovedad, Prestador, RegimenCosto, TarifaAnual, Periodo, TipoCaracter
from configuracion.models import Estrato
from configuracion.models import Ars
from configuracion.models import Eps
from configuracion.models import CapacidadExcepcional
from configuracion.models import AsociacionPrivada


class Grado(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class EscalaNacional(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    criterio_evaluacion = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class ValoracionLetra(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    valor_numerico = models.IntegerField()
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


# specifying choices

RANGO_SIMBOLO_MENOR = (
    (">", ">"),
    ("<", "<"),
    (">=", ">="),
    ("<=", "<="),
    ("=", "="),
)

RANGO_SIMBOLO_MAYOR = (
    (">", ">"),
    ("<", "<"),
    (">=", ">="),
    ("<=", "<="),
    ("=", "="),
)


# declaring a Equivalencia Model
class Equivalencia(models.Model):
    codigo = models.CharField(max_length=10)
    rango_numerico_menor = models.DecimalField(max_digits=18, decimal_places=1)
    rango_numerico_mayor = models.DecimalField(max_digits=18, decimal_places=1)
    rango_simbolo_menor = models.CharField(max_length=2, choices=RANGO_SIMBOLO_MENOR)
    rango_simbolo_mayor = models.CharField(max_length=10, choices=RANGO_SIMBOLO_MAYOR)
    valor_letra = models.ForeignKey(ValoracionLetra, on_delete=models.CASCADE)
    escala_nacional = models.ForeignKey(EscalaNacional, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.codigo


class Estudiante(models.Model):
    codigo = models.CharField(max_length=20)
    codigoMEN = models.CharField(max_length=20)
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=20)
    departamento_expedicion = models.ForeignKey(Departamento, on_delete=models.CASCADE,
                                                related_name='departamento_expedicion_set')
    municipio_expedicion = models.ForeignKey(Municipio, on_delete=models.CASCADE,
                                             related_name='municipio_expedicion_set')
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=True, null=False)
    departamento_nacimiento = models.ForeignKey(Departamento, on_delete=models.CASCADE,
                                                related_name='departamento_nacimiento_set')
    municipio_nacimiento = models.ForeignKey(Municipio, on_delete=models.CASCADE,
                                             related_name='municipio_nacimiento_set')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    factor_rh = models.ForeignKey(FactorRh, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    fotografia = models.ImageField('Fotografia', upload_to='fotografia/', max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=100)
    departamento_residencia = models.ForeignKey(Departamento, on_delete=models.CASCADE,
                                                related_name='departamento_residencia_set')
    municipio_residencia = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    zona_residencia = models.ForeignKey(Zona, on_delete=models.CASCADE,
                                        related_name='zona_residencia_set')
    localidad = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    estrato = models.ForeignKey(Estrato, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    sisben = models.ForeignKey(Sisben, on_delete=models.CASCADE)
    numero_sisben = models.CharField(max_length=30)
    eps = models.ForeignKey(Eps, on_delete=models.CASCADE)
    ars = models.ForeignKey(Ars, on_delete=models.CASCADE)
    poblacion_victima = models.ForeignKey(PoblacionVictimaConflicto, on_delete=models.CASCADE)
    departamento_expulsor = models.ForeignKey(Departamento, on_delete=models.CASCADE,
                                              related_name='departamento_expulsor_set', blank=True, null=True)
    municipio_expulsor = models.ForeignKey(Municipio, on_delete=models.CASCADE,
                                           related_name='municipio_expulsor_set', blank=True, null=True)
    fecha_expulsion = models.DateField(blank=True, null=True)
    certificado_expulsion = models.CharField(max_length=20, blank=True)
    fecha_certificado_expulsion = models.DateField(blank=True, null=True)
    tipo_discapacidad = models.ForeignKey(TipoDiscapacidad, on_delete=models.CASCADE)
    capacidad_excepcional = models.ForeignKey(CapacidadExcepcional, on_delete=models.CASCADE)
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
    resguardo = models.ForeignKey(Resguardo, on_delete=models.CASCADE)
    proviene_sector_privado = models.BooleanField(default=False)
    proviene_otro_municipio = models.BooleanField(default=False)
    institucion_bienestar = models.CharField(max_length=100, blank=True)

    tipo_identificacion_madre = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE,
                                                  related_name='tipo_identificacion_madre_set', blank=True, null=True)
    numero_documento_madre = models.CharField(max_length=20, blank=True)
    departamento_expedicion_madre = models.ForeignKey(Departamento, on_delete=models.CASCADE,
                                                      related_name='departamento_expedicion_madre_set', blank=True,
                                                      null=True)
    municipio_expedicion_madre = models.ForeignKey(Municipio, on_delete=models.CASCADE,
                                                   related_name='municipio_expedicion_madre_set', blank=True, null=True)
    primer_apellido_madre = models.CharField(max_length=20, blank=True)
    segundo_apellido_madre = models.CharField(max_length=20, blank=True)
    primer_nombre_madre = models.CharField(max_length=20, blank=True)
    segundo_nombre_madre = models.CharField(max_length=20, blank=True)
    email_madre = models.CharField(max_length=50, blank=True)
    direccion_madre = models.CharField(max_length=100, blank=True)
    departamento_residencia_madre = models.ForeignKey(Departamento, on_delete=models.CASCADE,
                                                      related_name='departamento_residencia_madre_set', blank=True,
                                                      null=True)
    municipio_residencia_madre = models.ForeignKey(Municipio, on_delete=models.CASCADE,
                                                   related_name='municipio_residencia_madre_set', blank=True, null=True)
    zona_residencia_madre = models.ForeignKey(Zona, on_delete=models.CASCADE,
                                              related_name='zona_residencia_madre_set', blank=True, null=True)
    barrio_madre = models.CharField(max_length=100, blank=True)
    localidad_madre = models.CharField(max_length=100, blank=True)
    telefono_madre = models.CharField(max_length=20, blank=True)
    celular_madre = models.CharField(max_length=20, blank=True)
    ocupacion_madre = models.CharField(max_length=100, blank=True)
    empresa_madre = models.CharField(max_length=100, blank=True)
    telefono_empresa_madre = models.CharField(max_length=20, blank=True)

    tipo_identificacion_padre = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE,
                                                  related_name='tipo_identificacion_padre_set', blank=True, null=True)
    numero_documento_padre = models.CharField(max_length=20, blank=True)
    departamento_expedicion_padre = models.ForeignKey(Departamento, on_delete=models.CASCADE, blank=True, null=True)
    municipio_expedicion_padre = models.ForeignKey(Municipio, on_delete=models.CASCADE,
                                                   related_name='municipio_expedicion_padre_set', blank=True, null=True)
    primer_apellido_padre = models.CharField(max_length=20, blank=True)
    segundo_apellido_padre = models.CharField(max_length=20, blank=True)
    primer_nombre_padre = models.CharField(max_length=20, blank=True)
    segundo_nombre_padre = models.CharField(max_length=20, blank=True)
    email_padre = models.CharField(max_length=50, blank=True)
    direccion_padre = models.CharField(max_length=100, blank=True)
    departamento_residencia_padre = models.ForeignKey(Departamento, on_delete=models.CASCADE,
                                                      related_name='departamento_residencia_padre_set', blank=True, null=True)
    municipio_residencia_padre = models.ForeignKey(Municipio, on_delete=models.CASCADE,
                                                   related_name='municipio_residencia_padre_set', blank=True, null=True)
    zona_residencia_padre = models.ForeignKey(Zona, on_delete=models.CASCADE,
                                              related_name='zona_residencia_padre_set', blank=True, null=True)
    barrio_padre = models.CharField(max_length=100, blank=True)
    localidad_padre = models.CharField(max_length=100, blank=True)
    telefono_padre = models.CharField(max_length=20, blank=True)
    celular_padre = models.CharField(max_length=20, blank=True)
    ocupacion_padre = models.CharField(max_length=100, blank=True)
    empresa_padre = models.CharField(max_length=100, blank=True)
    telefono_empresa_padre = models.CharField(max_length=20, blank=True)

    tipo_identificacion_acudiente = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE,
                                                      related_name='tipo_identificacion_acudiente_set')
    numero_documento_acudiente = models.CharField(max_length=20)
    departamento_expedicion_acudiente = models.ForeignKey(Departamento, on_delete=models.CASCADE,
                                                          related_name='departamento_expedicion_acudiente_set')
    municipio_expedicion_acudiente = models.ForeignKey(Municipio, on_delete=models.CASCADE,
                                                       related_name='municipio_expedicion_acudiente_set')
    primer_apellido_acudiente = models.CharField(max_length=20)
    segundo_apellido_acudiente = models.CharField(max_length=20)
    primer_nombre_acudiente = models.CharField(max_length=20)
    segundo_nombre_acudiente = models.CharField(max_length=20)
    email_acudiente = models.CharField(max_length=50)
    direccion_acudiente = models.CharField(max_length=100)
    departamento_residencia_acudiente = models.ForeignKey(Departamento, on_delete=models.CASCADE,
                                                          related_name='departamento_residencia_acudiente_set')
    municipio_residencia_acudiente = models.ForeignKey(Municipio, on_delete=models.CASCADE,
                                                       related_name='municipio_residencia_acudiente_set')
    zona_residencia_acudiente = models.ForeignKey(Zona, on_delete=models.CASCADE,
                                                  related_name='zona_residencia_acudiente_set')
    barrio_acudiente = models.CharField(max_length=100)
    localidad_acudiente = models.CharField(max_length=100)
    telefono_acudiente = models.CharField(max_length=20)
    celular_acudiente = models.CharField(max_length=20)
    ocupacion_acudiente = models.CharField(max_length=100)
    empresa_acudiente = models.CharField(max_length=100, blank=True)
    telefono_empresa_acudiente = models.CharField(max_length=20)
    genero_acudiente = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='genero_acudiente_set')
    parentesco_acudiente = models.ForeignKey(Parentesco, on_delete=models.CASCADE)
    colegio_ultimo_curso = models.CharField(max_length=100, blank=True)
    direccion_colegio_ultimo_curso = models.CharField(max_length=100, blank=True)
    telefono_colegio_ultimo_curso = models.CharField(max_length=20, blank=True)
    ultimo_grado = models.CharField(max_length=20, blank=True)
    anio = models.CharField(max_length=4, blank=True)
    motivo_retiro_ultimo = models.CharField(max_length=255, blank=True)
    observaciones = models.TextField(blank=True)
    usuario_estudiante = models.CharField(max_length=20)
    clave_acceso = models.CharField(max_length=20)
    grupo_usuario = models.ForeignKey(Group, on_delete=models.CASCADE)
    seleccione_madre = models.BooleanField(default=False)
    seleccione_padre = models.BooleanField(default=False)
    seleccione_acudiente = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.codigoMEN


class Nucleo(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    nombre_director = models.CharField(max_length=30)
    telefono_director = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Institucion(models.Model):
    codigo = models.CharField(max_length=10)
    codigo_dane = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    nombre_rector = models.CharField(max_length=100)
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    tipo_sector_educacion = models.ForeignKey(TipoSectorEducacion, on_delete=models.CASCADE)
    propiedad_juridica = models.ForeignKey(PropiedadJuridica, on_delete=models.CASCADE)
    numero_sedes = models.IntegerField()
    nucleo = models.ForeignKey(Nucleo, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='genero_set')
    subsidio = models.BooleanField(default=False)
    tipo_discapacidad = models.ForeignKey(TipoDiscapacidad, on_delete=models.CASCADE)
    capacidad_excepcional = models.ForeignKey(CapacidadExcepcional, on_delete=models.CASCADE)
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
    resguardo = models.ForeignKey(Resguardo, on_delete=models.CASCADE)
    tipo_novedad = models.ForeignKey(TipoNovedad, on_delete=models.CASCADE)
    metodologia = models.ForeignKey(Metodologia, on_delete=models.CASCADE)
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    decreto_creacion = models.CharField(max_length=30)
    director = models.CharField(max_length=100)
    secretaria = models.CharField(max_length=100)
    aprobacion = models.CharField(max_length=30)
    lema = models.CharField(max_length=255)
    escudo = models.ImageField('Escudo', upload_to='escudo/', max_length=200, blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    barrio = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, blank=True)
    sitio_web = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=50)
    numero_liciencia = models.CharField(max_length=10)
    regimen_costo = models.ForeignKey(RegimenCosto, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    asociacion_privada = models.ForeignKey(AsociacionPrivada, on_delete=models.CASCADE)
    tarifa_anual = models.ForeignKey(TarifaAnual, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'
        ordering = ['codigo']


class Profesor(models.Model):
    codigo = models.CharField(max_length=10)
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    escalafon = models.ForeignKey(Escalafon, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def fullname(self):
        # return '{} {}'.format(self.primer_apellido, self.segundo_apellido)
        return f'{self.primer_apellido} {self.segundo_apellido}'  # with python 3.6+

    def __str__(self):
        return self.codigo


class Curso(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    jornda = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    intensidad_horaria = models.IntegerField()
    orden = models.IntegerField()
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Juicio(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Sede(models.Model):
    codigo = models.CharField(max_length=12)
    codigo_dane_nuevo = models.CharField(max_length=12)
    codigo_dane_antiguo = models.CharField(max_length=12)
    codigo_consecutivo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    barrio = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    tipo_novedad = models.ForeignKey(TipoNovedad, on_delete=models.CASCADE)
    jornada_completa = models.BooleanField(default=False)
    jornada_manana = models.BooleanField(default=False)
    jornada_tarde = models.BooleanField(default=False)
    jornada_noche = models.BooleanField(default=False)
    jornada_fin_semana = models.BooleanField(default=False)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(blank=True, null=False)
    director = models.CharField(max_length=30)
    secretaria = models.CharField(max_length=30)
    escala_valoracion_nacional = models.BooleanField(default=False)
    rango_numerico = models.BooleanField(default=False)
    numero_inicial = models.IntegerField()
    numero_final = models.IntegerField()
    valoracion_letras = models.BooleanField(default=False)
    juicios = models.BooleanField(default=False)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    edad_matricula = models.CharField(max_length=255)
    numero_matricula = models.CharField(max_length=255)
    numero_folio = models.CharField(max_length=255)
    fecha_matricula = models.DateField(blank=True, null=False)
    anio_matricula = models.DateField(blank=True, null=False)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    estado_matricula = models.IntegerField()
    repitente = models.BooleanField(default=False)
    tipo_caracter = models.ForeignKey(TipoCaracter, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    observaciones = models.TextField()
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.numero_matricula
