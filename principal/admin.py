from django.contrib import admin

from .models import Curso
from .models import Equivalencia
from .models import EscalaNacional
from .models import Estudiante
from .models import Institucion
from .models import Juicio
from .models import Materia
from .models import Matricula
from .models import Nucleo
from .models import Profesor
from .models import Sede
from .models import ValoracionLetra
from .models import Grado
from .models import Grupo


class GradoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'fullname')
    # ordering = ('codigo')

# https://stackoverflow.com/questions/57912707/is-there-a-way-to-concatenate-2-model-field-names-in-the-list-display-to-displ

admin.site.register(Curso)
admin.site.register(Equivalencia)
admin.site.register(EscalaNacional)
admin.site.register(Estudiante)
admin.site.register(Institucion)
admin.site.register(Juicio)
admin.site.register(Materia)
admin.site.register(Matricula)
admin.site.register(Nucleo)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Sede)
admin.site.register(ValoracionLetra)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Grupo)
