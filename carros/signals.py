from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from carros.models import Carro, CarroInventorio
from openai_api.cliente import get_carro_ai_bio


def carro_inventario_atualizar():
    carros_quantidade = Carro.objects.all().count()
    carros_valor = Carro.objects.aggregate(
        valor_total=Sum('valor')
    )['valor_total']
    CarroInventorio.objects.create(
        carros_quantidade=carros_quantidade,
        carros_valor=carros_valor
    )

@receiver(pre_save, sender=Carro)    
def carro_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = get_carro_ai_bio(
            instance.modelo, instance.marca, instance.ano_fabricacao
        )
        instance.bio = ai_bio

@receiver(post_save, sender=Carro)
def Carro_post_salva(sender, instance, **kwargs):
    carro_inventario_atualizar()


@receiver(post_delete, sender=Carro)
def carro_post_delete(sender, instance, **kwargs):
    carro_inventario_atualizar()