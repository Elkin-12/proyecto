from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    apellido = models.CharField(max_length=100,blank=False, null=False)
    email = models.EmailField(blank=False, null=False,help_text="Ingrese su correo electrónico ",unique=True)
    telefono = models.CharField(max_length=20,blank=False, null=False)
    direccion = models.CharField(max_length=200,blank=False, null=False)

    class tipo_documento(models.TextChoices):
        Tarjeta_Identidad = 'TI', 'Tarjeta de Identidad'
        cedula = 'CC', 'Cédula de Ciudadanía'
        pasaporte = 'PASSPORT', 'Pasaporte'
        otro = 'OTRO', 'Otro'
    tipo_documento = models.CharField(max_length=20, choices=tipo_documento.choices, default=tipo_documento.otro)
    numero_documento = models.CharField(max_length=50,blank=False, null=False,unique=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class meta:
        db_table = 'Tabla_de_clientes'
        verbose_name_plural = 'Clientes'

class Especialidades(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    def __str__(self):
        return self.nombre
    class meta:
        db_table = 'Tabla_de_especialidades'
        verbose_name_plural = 'Especialidades'

class Servicio(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    def __str__(self):
        return self.nombre
    class meta:
        db_table = 'Tabla_de_servicios'
        verbose_name_plural = 'Servicios'

class Medico(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    apellido = models.CharField(max_length=100,blank=False, null=False)
    especialidad = models.ManyToManyField(Especialidades, related_name='medicos')
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class meta:
        db_table = 'Tabla_de_medicos'
        verbose_name_plural = 'Medicos'

class Cita(models.Model):
    fecha_hora = models.DateTimeField()
    class estado_cita(models.TextChoices):
        pendiente = 'PENDIENTE', 'Pendiente'
        confirmada = 'CONFIRMADA', 'Confirmada'
        cancelada = 'CANCELADA', 'Cancelada'
    estado = models.CharField(max_length=20, choices=estado_cita.choices, default=estado_cita.pendiente)
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT, related_name='citas')
    medico = models.ForeignKey(Medico,on_delete=models.PROTECT, related_name='citas')
    servicio = models.ForeignKey(Servicio,on_delete=models.PROTECT, related_name='citas')
    def __str__(self):
        fecha_formateada = self.fecha_hora.strftime('%d/%m/%Y %H:%M')
        return f"Cita [{fecha_formateada}] - {self.servicio.nombre} | Paciente: {self.cliente} | Dr(a). {self.medico.apellido}"
    class meta:
        db_table = 'Tabla_de_citas'
        verbose_name_plural = 'Citas'

