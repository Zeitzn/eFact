from django.db import models

# Create your models here.
class Cliente(models.Model):
    
    
    ruc = models.CharField(unique=True,max_length=12)
    razon_social = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.razon_social

    @property
    def p_razon_social(self):
        return '%s %s %s' % (self.razon_social)