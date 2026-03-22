from django.contrib import admin
from .models import Empresa, Funcionario, Departamento, Documento, RegistroHoraExtra


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')


@admin.register(RegistroHoraExtra)
class RegistroHoraExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'motivo')
