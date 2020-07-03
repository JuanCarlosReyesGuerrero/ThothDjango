from django.db import models
from django.utils import timezone

class AporteParafiscal(models.Model):
    codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = "Aporte Parafiscal"
        verbose_name_plural = "Aportes Parafiscales"

    def __str__(self):
        return self.nombre

class Ars(models.Model):
    codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length=255)
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


class Asignatura(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class AsociacionPrivada(models.Model):
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=255)
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


class Calendario(models.Model):
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=255)
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


class CapacidadExcepcional(models.Model):
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=255)
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


class Cargo(models.Model):
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=255)
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


class ClaseFuncionario(models.Model):
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=255)
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


class Departamento(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=255)
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


class Eps(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class Escalafon(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class Especialidad(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class EstadoCivil(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class Estrato(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class Etnia(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class FactorRh(models.Model):
    codigo = models.CharField(max_length=3)
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


class FuenteRecurso(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Genero(models.Model):
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


class GeneroEstudiante(models.Model):
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


class GrupoUsuario(models.Model):
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


class Idioma(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)
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


class Jornada(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class LibretaMilitar(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Metodologia(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Municipio(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=255)
    codigo_unificado = models.CharField(max_length=6)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    departamento_codigo = models.CharField(max_length=2)
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


class NivelEducativo(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class NivelEducativoDocente(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Parentesco(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Perfil(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Periodo(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class PoblacionVictimaConflicto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Prestador(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Profesion(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class PropiedadJuridica(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Rango(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class RegimenCosto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Resguardo(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class Sisben(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
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


class SituacionAcademica(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TarifaAnual(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TipoAcademica(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TipoCaracter(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TipoCondicion(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TipoDevengo(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TipoDiscapacidad(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TipoIdentificacion(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TipoNovedad(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TipoRespuesta(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TipoSectorEducacion(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class TipoVinculacion(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
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


class Zona(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=10)
    Descripcion = models.CharField(max_length=10)
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