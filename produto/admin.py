from django.contrib import admin
from . import models

class VaricaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta', 'get_preco_formatado', 'get_preco_formatado_promocional']
    inlines = [
        VaricaoInline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)