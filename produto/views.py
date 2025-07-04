from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista Produtos')


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe Produtos')


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar Carrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover Carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')