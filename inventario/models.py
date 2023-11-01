from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.conf import settings

class Empresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nro_documento = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)

class Sucursal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre_comercial = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)

class Personal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nombre_personal = models.CharField(max_length=100)
    direccion_personal = models.CharField(max_length=150)
    tipo_documento = models.IntegerField(choices=(
        (1, 'DNI'),
        (2, 'Carnet de Extranjería'),
        (3, 'Otro'),
    ))
    nro_documento = models.CharField(max_length=11)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class GrupoProveedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    codigo_grupo = models.CharField(max_length=15)
    grupo_descripcion = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    responsable_grupo = models.ForeignKey(Personal, on_delete=models.CASCADE)

class LineaArticulo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    codigo_linea = models.CharField(max_length=15)
    linea_descripcion = models.CharField(max_length=100)
    grupo = models.ForeignKey(GrupoProveedor, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    responsable_linea = models.ForeignKey(Personal, on_delete=models.CASCADE)

class SublineaArticulo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    codigo_sublinea = models.CharField(max_length=15)
    sublinea_descripcion = models.CharField(max_length=100)
    linea = models.ForeignKey(LineaArticulo, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

class UnidadMedida(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    unidad_nombre = models.CharField(max_length=150)

class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    codigo_marca = models.CharField(max_length=14)
    marca_nombre = models.CharField(max_length=150)

class Articulo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    codigo_sku = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=150)
    codigo_sublinea = models.CharField(max_length=15)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GrupoProveedor, on_delete=models.CASCADE)
    linea = models.ForeignKey(LineaArticulo, on_delete=models.CASCADE)
    sublinea = models.ForeignKey(SublineaArticulo, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    factor_compra = models.IntegerField()
    factor_reparto = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

  
class Inventario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha_inventario = models.DateTimeField()
    nro_inventario = models.IntegerField()
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    hora_inicio = models.TimeField()  # Formato "hh:mm AM/PM"
    hora_fin = models.TimeField()
    total_inventario = models.DecimalField(max_digits=12, decimal_places=2)
    ESTADOS = (
        ('P', 'Pending'),
        ('IP', 'In Progress'),
        ('C', 'Closed'),
    )
    
    estado = models.CharField(max_length=2, choices=ESTADOS, default='P')
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='inventarios_registrados', null=True)
    cerrado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='inventarios_cerrados', null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('fecha_inventario', 'empresa', 'sucursal')


class ItemInventario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    nro_item = models.IntegerField()
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    stock_fisico = models.DecimalField(max_digits=12, decimal_places=2)
    devoluciones_pendientes = models.DecimalField(max_digits=12, decimal_places=2)
    total_unidades_stock = models.DecimalField(max_digits=12, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=12, decimal_places=2)
    total_item = models.DecimalField(max_digits=12, decimal_places=2)

class Usuario(AbstractUser):
    username= None
    email = models.EmailField(_("email address"), unique=True)
    fullname = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=150, null=True)
    objects = CustomUserManager()
      
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['fullname']
        
    def __str__(self):
        return self.email