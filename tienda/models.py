from django.db import models
from django.contrib.auth.models import User

class Peluches(models.Model):
    producto   = models.CharField(max_length=50)
    foto       = models.ImageField(upload_to="media/Peluches/", default= "default_Models.png")
    precio     = models.FloatField()
    en_stock   = models.BooleanField()
    disponibles= models.IntegerField()  
    class Meta:
        verbose_name = "Peluche"
        verbose_name_plural = "Peluches"
        ordering = ["precio"]
    def __str__(self):
        return f"{self.producto}"

class Cartas(models.Model):
    juego      = models.CharField(max_length=50)
    adultos    = models.BooleanField() #Si el juego es para +18
    cantCartas = models.IntegerField()
    foto       = models.ImageField(upload_to="media/Cartas/",default= "default_Models.png")
    precio     = models.FloatField()
    en_stock   = models.BooleanField()
    disponibles= models.IntegerField()
    class Meta:
        verbose_name = "Juego de Cartas"
        verbose_name_plural = "Juegos de Cartas"
        ordering = ["precio"]
    def __str__(self):
        if self.adultos == True:
            return f"{self.juego} (+18)"
        else:
            return f"{self.juego}"

class Juegos_de_Mesa(models.Model):
    juego      = models.CharField(max_length=50)
    adultos    = models.BooleanField()
    piezas     = models.IntegerField()
    foto       = models.ImageField(upload_to="media/Mesa/",default= "default_Models.png")
    precio     = models.FloatField()
    en_stock   = models.BooleanField()
    disponibles= models.IntegerField()
    class Meta:
        verbose_name = "Juego de Mesa"
        verbose_name_plural = "Juegos de Mesa"
        ordering = ["precio"]
    def __str__(self):
        if self.adultos == True:
            return f"{self.juego} (+18)"
        else:
            return f"{self.juego}"
        
class Figura_de_Accion(models.Model):
    figura     = models.CharField(max_length=50)
    origen     = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    foto       = models.ImageField(upload_to="media/Figuras/",default= "default_Models.png")
    precio     = models.FloatField()
    en_stock   = models.BooleanField()
    disponibles= models.IntegerField()
    class Meta:
        verbose_name = "Figura de Acción"
        verbose_name_plural = "Figuras de Acción"
        ordering = ["precio"]
    def __str__(self):
        return f"{self.figura}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatar", default="default.png")
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.user} {self.imagen}"
