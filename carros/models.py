from django.db import models


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='Carro_Marca')
    ano_fabricacao = models.IntegerField(blank=True, null=True)
    modelo_ano = models.IntegerField(blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    foto = models.ImageField(upload_to='carros/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.modelo
    
class CarroInventorio(models.Model):
    carros_quantidade = models.IntegerField()
    carros_valor = models.FloatField()
    data_registro = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-data_registro']


    def __str__(self):
        return f'{self.carros_quantidade} - {self.carros_valor}'


