from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum, Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Empresa, Funcionario, Departamento, Documento, RegistroHoraExtra
from .forms import EmpresaForm, FuncionarioForm, DepartamentoForm, DocumentoForm, RegistroHoraExtraForm 


class DashboardView(TemplateView):
    template_name = 'rh/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # INDICADORES TOTAIS
        context['total_funcionarios'] = Funcionario.objects.count()
        context['total_empresas'] = Empresa.objects.count()
        context['total_documentos'] = Documento.objects.count()
        
        # SOMA DE TODAS AS HORAS EXTRAS REGISTRADAS
        soma_horas = RegistroHoraExtra.objects.aggregate(total=Sum('horas'))['total']
        context['total_horas_extras'] = soma_horas or 0
        
        # LISTA RÁPIDA: ÚLTIMOS 5 LANÇAMENTOS
        context['ultimas_horas'] = RegistroHoraExtra.objects.select_related('funcionario').all().order_by('-id')[:5]
        
        return context

# ==========================================
# VIEWS DE EMPRESA (UNIDADES)
# ==========================================

class EmpresaList(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'rh/empresa_list.html'
    context_object_name = 'empresas'
    ordering = ['nome']

class EmpresaDetail(LoginRequiredMixin, DetailView):
    model = Empresa
    template_name = 'rh/empresa_detail.html'
    context_object_name = 'empresa'

class EmpresaCreate(LoginRequiredMixin, CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'rh/empresa_form.html'
    success_url = reverse_lazy('list_empresas')

class EmpresaUpdate(LoginRequiredMixin, UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'rh/empresa_form.html'
    success_url = reverse_lazy('list_empresas')

class EmpresaDelete(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = 'rh/empresa_confirm_delete.html'
    success_url = reverse_lazy('list_empresas')


# ==========================================
# VIEWS DE FUNCIONÁRIO (AGENTES)
# ==========================================

class FuncionarioList(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'rh/funcionario_list.html'
    context_object_name = 'funcionarios'

    queryset = Funcionario.objects.select_related('empresa').all()

class FuncionarioCreate(LoginRequiredMixin, CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'rh/funcionario_form.html'
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioUpdate(LoginRequiredMixin, UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'rh/funcionario_form.html'
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioDelete(LoginRequiredMixin, DeleteView):
    model = Funcionario
    template_name = 'rh/funcionario_confirm_delete.html'
    success_url = reverse_lazy('list_funcionarios')

# ==========================================
# VIEWS DE DEPARTAMENTO 
# ==========================================

class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'rh/departamento_list.html' # Caminho: rh/templates/rh/departamento_list.html
    context_object_name = 'departamentos'

class DepartamentoCreateView(CreateView):
    model = Departamento
    form_class = DepartamentoForm 
    template_name = 'rh/departamento_form.html'
    success_url = reverse_lazy('list_departamentos')


class DepartamentoUpdateView(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'rh/departamento_form.html'
    success_url = reverse_lazy('list_departamentos')


class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = 'rh/departamento_confirm_delete.html'
    success_url = reverse_lazy('list_departamentos')   


# ==========================================
# VIEWS DE DOCUMENTO
# ==========================================     

class DocumentoListView(ListView):
    model = Documento
    template_name = 'rh/documento_list.html'
    context_object_name = 'documentos'
    ordering = ['-id']


class DocumentoCreateView(CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'rh/documento_form.html'
    success_url = reverse_lazy('list_funcionarios')


    def get_initial(self):
        initial = super().get_initial()
        funcionario_id = self.request.GET.get('funcionario_id')
        if funcionario_id:
            initial['pertence'] = funcionario_id
        return initial


class DocumentoDeleteView(DeleteView):
    model = Documento
    template_name = 'rh/documento_confirm_delete.html'
    success_url = reverse_lazy('list_funcionarios')

# ==========================================
# VIEWS HORAS EXTRAS
# ==========================================

class HoraExtraListView(ListView):
    model = RegistroHoraExtra
    template_name = 'rh/horaextra_list.html'
    context_object_name = 'horas'
    ordering = ['-id'] 


class HoraExtraCreateView(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    template_name = 'rh/horaextra_form.html'
    success_url = reverse_lazy('list_horas')

    def get_initial(self):
        initial = super().get_initial()
        funcionario_id = self.request.GET.get('funcionario_id')
        if funcionario_id:
            initial['funcionario'] = funcionario_id
        return initial


class HoraExtraDeleteView(DeleteView):
    model = RegistroHoraExtra
    template_name = 'rh/horaextra_confirm_delete.html'
    success_url = reverse_lazy('list_horas')    