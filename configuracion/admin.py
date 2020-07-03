from django.contrib import admin

from .models import AporteParafiscal
from .models import Ars
from .models import Asignatura
from .models import AsociacionPrivada
from .models import Calendario
from .models import CapacidadExcepcional
from .models import Cargo
from .models import ClaseFuncionario
from .models import Departamento
from .models import Eps
from .models import Escalafon
from .models import Especialidad
from .models import EstadoCivil
from .models import Estrato
from .models import Etnia
from .models import FactorRh
from .models import FuenteRecurso
from .models import Genero
from .models import GeneroEstudiante
from .models import GrupoUsuario
from .models import Idioma
from .models import Jornada
from .models import LibretaMilitar
from .models import Metodologia
from .models import Municipio
from .models import NivelEducativo
from .models import NivelEducativoDocente
from .models import Parentesco
from .models import Perfil
from .models import Periodo
from .models import PoblacionVictimaConflicto
from .models import Prestador
from .models import Profesion
from .models import PropiedadJuridica
from .models import Rango
from .models import RegimenCosto
from .models import Resguardo
from .models import Sisben
from .models import SituacionAcademica
from .models import TarifaAnual
from .models import TipoAcademica
from .models import TipoCaracter
from .models import TipoCondicion
from .models import TipoDevengo
from .models import TipoDiscapacidad
from .models import TipoIdentificacion
from .models import TipoNovedad
from .models import TipoRespuesta
from .models import TipoSectorEducacion
from .models import TipoVinculacion
from .models import Zona


class AporteParafiscalAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class ArsAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class AsociacionPrivadaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class CapacidadExcepcionalAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class CargoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class ClaseFuncionarioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class EpsAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class EscalafonAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class EstratoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class EtniaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class FactorRhAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class FuenteRecursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class GeneroEstudianteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class GrupoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class IdiomaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class JornadaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class LibretaMilitarAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class MetodologiaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class MunicipioAdmin(admin.ModelAdmin):
    model = Municipio
    list_display = ('codigo_unificado', 'nombre', 'get_name')
    ordering = ('codigo_unificado', 'nombre', 'departamento__nombre')

    def get_name(self, obj):
        return obj.departamento.nombre

    get_name.admin_order_field = 'departamento'  # Allows column order sorting
    get_name.short_description = 'Departamento'  # Renames column head

    # get_name.admin_order_field = 'departamento__nombre'

    # Filtering on side - for some reason, this works
    # list_filter = ['title', 'author__name']


class NivelEducativoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class NivelEducativoDocenteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class ParentescoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class PoblacionVictimaConflictoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class PrestadorAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class ProfesionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class PropiedadJuridicaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class RangoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class RegimenCostoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class ResguardoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class SisbenAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class SituacionAcademicaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TarifaAnualAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TipoAcademicaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TipoCaracterAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TipoCondicionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TipoDevengoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TipoDiscapacidadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TipoIdentificacionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TipoNovedadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TipoRespuestaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TipoSectorEducacionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class TipoVinculacionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class ZonaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


admin.site.register(AporteParafiscal, AporteParafiscalAdmin)
admin.site.register(Ars, ArsAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(AsociacionPrivada, AsociacionPrivadaAdmin)
admin.site.register(Calendario, CalendarioAdmin)
admin.site.register(CapacidadExcepcional, CapacidadExcepcionalAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(ClaseFuncionario, ClaseFuncionarioAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Eps, EpsAdmin)
admin.site.register(Escalafon, EscalafonAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(EstadoCivil, EstadoCivilAdmin)
admin.site.register(Estrato, EstratoAdmin)
admin.site.register(Etnia, EtniaAdmin)
admin.site.register(FactorRh, FactorRhAdmin)
admin.site.register(FuenteRecurso, FuenteRecursoAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(GeneroEstudiante, GeneroEstudianteAdmin)
admin.site.register(GrupoUsuario, GrupoUsuarioAdmin)
admin.site.register(Idioma, IdiomaAdmin)
admin.site.register(Jornada, JornadaAdmin)
admin.site.register(LibretaMilitar, LibretaMilitarAdmin)
admin.site.register(Metodologia, MetodologiaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(NivelEducativo, NivelEducativoAdmin)
admin.site.register(NivelEducativoDocente, NivelEducativoDocenteAdmin)
admin.site.register(Parentesco, ParentescoAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(PoblacionVictimaConflicto, PoblacionVictimaConflictoAdmin)
admin.site.register(Prestador, PrestadorAdmin)
admin.site.register(Profesion, ProfesionAdmin)
admin.site.register(PropiedadJuridica, PropiedadJuridicaAdmin)
admin.site.register(Rango, RangoAdmin)
admin.site.register(RegimenCosto, RegimenCostoAdmin)
admin.site.register(Resguardo, ResguardoAdmin)
admin.site.register(Sisben, SisbenAdmin)
admin.site.register(SituacionAcademica, SituacionAcademicaAdmin)
admin.site.register(TarifaAnual, TarifaAnualAdmin)
admin.site.register(TipoAcademica, TipoAcademicaAdmin)
admin.site.register(TipoCaracter, TipoCaracterAdmin)
admin.site.register(TipoCondicion, TipoCondicionAdmin)
admin.site.register(TipoDevengo, TipoDevengoAdmin)
admin.site.register(TipoDiscapacidad, TipoDiscapacidadAdmin)
admin.site.register(TipoIdentificacion, TipoIdentificacionAdmin)
admin.site.register(TipoNovedad, TipoNovedadAdmin)
admin.site.register(TipoRespuesta, TipoRespuestaAdmin)
admin.site.register(TipoSectorEducacion, TipoSectorEducacionAdmin)
admin.site.register(TipoVinculacion, TipoVinculacionAdmin)
admin.site.register(Zona, ZonaAdmin)
