from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

estados_perro = (
    ('rescatado','RESCATADO'),
    ('disponible','DISPONIBLE'),
    ('adoptado','ADOPTADO')
)
class Perro(models.Model):
    fotografia      = models.ImageField(upload_to="media")
    nombre          = models.CharField("Nombre", max_length=200)
    raza            = models.CharField("Raza", max_length=200)
    descripcion	    = models.TextField("Descripción" )
    estado          = models.CharField(max_length=50, choices=estados_perro, default='rescatado')
    adoptador_por   = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    published_date  = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.nombre

class Adopcion(models.Model):
    Perro = models.ForeignKey(Perro, null=False, blank=False, on_delete=models.CASCADE,)
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.User, self.Perro)

class BlogPost(models.Model):
    img             = models.ImageField(upload_to="blog")
    titulo          = models.CharField("Titulo", max_length=200)
    subtitulo       = models.CharField("Subtitulo", max_length=200, null=True)
    contenido       = models.TextField("Contenido" )
    
    enlace_externo_titulo  = models.CharField("Titulo_enlace", max_length=200, null=True)
    enlace_externo  = models.URLField("Enlace externo", max_length=200, null=True)
    
    published_date  = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.titulo

class Slider(models.Model):
    img             = models.ImageField(upload_to="slider")
    descripcion       = models.TextField("descripcion" )
    published_date  = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.descripcion