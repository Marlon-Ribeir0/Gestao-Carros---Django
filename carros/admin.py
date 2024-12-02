from django.contrib import admin
from carros.models import Carro, Marca

class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabricacao', 'modelo_ano', 'valor')
    search_fields = ('modelo', 'marca')




class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    

admin.site.register(Carro, CarroAdmin)
admin.site.register(Marca, MarcaAdmin)

