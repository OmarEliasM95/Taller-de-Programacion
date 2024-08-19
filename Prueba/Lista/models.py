from django.db import models
class producto(models.Model):
    Nombre=models.CharField(max_length=100)
    Precio=models.DecimalField(max_digits=8, decimal_places=2)
    Existencias=models.IntegerField()
    def __str__(self):
        return f"{self.Nombre}"
