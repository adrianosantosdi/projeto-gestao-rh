from django import forms
from django.contrib.auth.models import User
from .models import Empresa, Funcionario, Departamento, Documento, RegistroHoraExtra


INPUT_STYLE = 'w-full bg-slate-950 border border-slate-800 text-slate-200 text-sm rounded-xl focus:ring-2 focus:ring-blue-600 focus:border-transparent p-3 outline-none transition-all placeholder:text-slate-600 shadow-inner'
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:ring-2 focus:ring-blue-500 outline-none transition-all font-mono',
                'placeholder': 'Designação da Unidade'
            }),
            'cnpj': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:ring-2 focus:ring-blue-500 outline-none transition-all font-mono',
                'placeholder': '00.000.000/0001-00'
            }),
        }

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        # CAMPOS REAIS DO SEU MODEL (SEM CPF)
        fields = ['nome', 'user', 'empresa', 'departamentos']
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:ring-2 focus:ring-blue-500 outline-none transition-all font-mono',
                'placeholder': 'Nome do Agente'
            }),
            'user': forms.Select(attrs={
                'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:ring-2 focus:ring-blue-500 outline-none transition-all font-mono'
            }),
            'empresa': forms.Select(attrs={
                'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:ring-2 focus:ring-blue-500 outline-none transition-all font-mono'
            }),
            'departamentos': forms.SelectMultiple(attrs={
                'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:ring-2 focus:ring-blue-500 outline-none transition-all font-mono h-32',
                'help_text': 'Mantenha CTRL pressionado para selecionar vários'
            }),
        }


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome', 'empresa']
        
        # Aqui é onde a mágica acontece para o Departamento ficar igual
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': INPUT_STYLE, 
                'placeholder': 'Digite o nome do setor...'
            }),
            'empresa': forms.Select(attrs={
                'class': INPUT_STYLE
            }),
        }
        
        # Labels amigáveis
        labels = {
            'nome': 'Nome do Departamento',
            'empresa': 'Unidade Responsável',
        }


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['descricao', 'arquivo', 'pertence']
        
        widgets = {
            'descricao': forms.TextInput(attrs={'class': INPUT_STYLE, 'placeholder': 'Ex: Contrato de Trabalho, RG...'}),
            'arquivo': forms.FileInput(attrs={'class': f"{INPUT_STYLE} file:bg-blue-600 file:border-none file:text-white file:px-4 file:py-1 file:rounded-lg file:text-[10px] file:uppercase file:font-black file:cursor-pointer"}),
            'pertence': forms.Select(attrs={'class': INPUT_STYLE}),
        }        



class RegistroHoraExtraForm(forms.ModelForm):
    class Meta:
        model = RegistroHoraExtra
        fields = ['funcionario', 'horas', 'motivo'] # Data é automática
        
        widgets = {
            'funcionario': forms.Select(attrs={'class': INPUT_STYLE}),
            'horas': forms.NumberInput(attrs={'class': INPUT_STYLE, 'placeholder': 'Ex: 2.5', 'step': '0.1'}),
            'motivo': forms.TextInput(attrs={'class': INPUT_STYLE, 'placeholder': 'Ex: Fechamento de folha...'}),
        }        