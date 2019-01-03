from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Usuario(models.Model):
    # dni = models.IntegerField(
    #     primary_key=True,
    #     validators=[MinValueValidator(10000000),
    #     MaxValueValidator(99999999)],
    #     )

    # dni=models.IntegerField(unique=True,validators=[MinValueValidator(10000000), MaxValueValidator(99999999)])
    ruc=models.CharField(unique=True,max_length=10)
    razon_social = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    # foto_perfil = models.ImageField(blank=True, upload_to='usuario', default='usuario/Koala.jpg')
    # numero_cuenta = models.CharField(max_length=100,unique=True)
    activo = models.BooleanField(default=True)

    usuario_login = models.OneToOneField(User, on_delete=models.PROTECT,null=True)
    # entidad_bancaria = models.ForeignKey(Entidad_bancaria, on_delete=models.PROTECT)
    # dni_referido = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    # depositos_pendientes=models.IntegerField(default=1,null=True)

    def __str__(self):
        return self.nombres

    @property
    def nombre_completo(self):
        return '%s %s %s' % (self.nombres, self.apellido_paterno, self.apellido_materno)
