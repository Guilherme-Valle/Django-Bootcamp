from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ProdutoForm
from .models import Produto
# Create your views here.

# REDIRECIONAR

def home(request):
    template = loader.get_template('appEstoque/home.html')
    return HttpResponse(template.render())
    pass


def cadastro(request):
    form = ProdutoForm()
    return render(request, 'appEstoque/cadastro.html',
                  {'form': form})
    pass


def lista(request):
    produtos = Produto.objects.all()
    return render(request, 'appEstoque/lista.html', {'produtos': produtos})
    pass


# HTTP -> Request
def cadastrar(request):
    try:
        if request.method == 'POST':
            form = ProdutoForm(request.POST)
            if form.is_valid():
                produto = Produto()
                produto.nome = form.cleaned_data['nome']
                produto.preco = form.cleaned_data['preco']
                produto.quantidade = form.cleaned_data['quantidade']
                produto.save()
                msg = 'Produto cadastrado com sucesso'
                return render(request, 'appEstoque/cadastro.html',
                              {'form': ProdutoForm(),
                               'msg': msg})
            else:
                return render(request, 'appEstoque/cadastro.html',
                              {'form': ProdutoForm(),
                               'msg': form.errors})
        else:
            raise Exception('Use POST para formulários',
                            'MethodEnvioError')
        return render(request, 'appEstoque/cadastro.html',
                      {'form' : ProdutoForm()})
    except Exception as ex:
        msg = ex

        return render(request, 'appEstoque/cadastro.html',
                      {'form': ProdutoForm(),
                       'msg': msg})
    pass



