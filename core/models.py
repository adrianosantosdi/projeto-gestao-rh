from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome
    

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.nome} ({self.empresa.nome})"
    

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
    

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='documentos/')
    pertence = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.descricao
    

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.funcionario.nome} - {self.horas}h"