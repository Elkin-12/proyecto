from django.contrib import admin
from .models import Cliente, Especialidades, Servicio, Medico, Cita
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'direccion', 'tipo_documento', 'numero_documento')
    search_fields = ('nombre', 'apellido', 'email', 'numero_documento')
@admin.register(Especialidades)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'especialidad_list')
    def especialidad_list(self, obj):
        return ", ".join([especialidad.nombre for especialidad in obj.especialidad.all()])
    search_fields = ('nombre', 'apellido', 'especialidad__nombre')
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('fecha_hora', 'estado', 'cliente', 'medico', 'servicio')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'medico__nombre', 'medico__apellido', 'servicio__nombre')
# Register your models here.
