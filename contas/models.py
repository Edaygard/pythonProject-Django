from django.db import models


# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=100)
    dt_criation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transacao(models.Model):
    data = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    obs = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        return self.description



