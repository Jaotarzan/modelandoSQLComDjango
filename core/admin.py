from django.contrib import admin

# Register your models here.
from .models import categoria, TipoAtuacao, pais, produtora, membro, filme, Atuacao

admin.site.register(categoria)
admin.site.register(TipoAtuacao)
admin.site.register(pais)
admin.site.register(produtora)
#admin.site.register(membro)
#admin.site.register(filme)
#admin.site.register(Atuacao)

class AtuacaoInline(admin.TabularInline):
    model = Atuacao

@admin.register(membro)
class MembroAdmin(admin.ModelAdmin):
    inlines :list[type(AtuacaoInline)] = [AtuacaoInline]

@admin.register(filme)
class FilmeAdmin(admin.ModelAdmin):
    inlines :list[type(AtuacaoInline)] = [AtuacaoInline]