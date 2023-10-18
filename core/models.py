from django.db import models

# Create your models here.
class categoria(models.Model):
    descricao = models.CharField(max_length=40)

    def __str__(self):
        return self.descricao
    
class TipoAtuacao(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = 'Tipos de atuação'
    
class pais(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Países'

class produtora(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(pais, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome
    
class membro(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    pais = models.ForeignKey(pais, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
    
class filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    sinopse = models.TextField()
    classificacao = models.IntegerField()
    duracao = models.TimeField()
    produtora = models.ForeignKey(produtora, on_delete=models.PROTECT)
    categorias = models.ManyToManyField(categoria)

    def __str__(self):
        return f"{self.titulo} ({self.ano})"
    
class Atuacao(models.Model):
    filme = models.ForeignKey(filme, on_delete=models.PROTECT)
    membro = models.ForeignKey(membro, on_delete=models.PROTECT)
    TipoAtuacao = models.ForeignKey(TipoAtuacao, on_delete=models.PROTECT)
    personagem = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.filme} - {self.membro} ({self.personagem})"