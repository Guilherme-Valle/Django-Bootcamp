from django import forms

class ProdutoForm(forms.Form):
    nome = forms.CharField(label="Digite o nome ",
                           max_length=100)

    preco = forms.FloatField(label="Digite o preço ")

    quantidade = forms.IntegerField(label="Digite a quantidade ")
    pass
