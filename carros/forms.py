from django import forms
from carros.models import Carro

class carroModelForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'

    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor < 10000:
            self.add_error('valor', 'Valor minimo do carro deve ser de R$10.000,00')
        return valor
    
    def clean_ano_fabricacao(self):
        ano_fabricacao = self.cleaned_data.get('ano_fabricacao')
        if ano_fabricacao < 1975:
            self.add_error('ano_fabricacao', 'Nao e possivel cadastrar carro abaixo do ano de 1975')
        return ano_fabricacao