from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ---------------------------------------------------------
    # DASHBOARD (PÁGINA INICIAL DO SISTEMA)
    # ---------------------------------------------------------
    # Definindo como a rota raiz ('') para ser a primeira tela ao logar
    path('', views.DashboardView.as_view(), name='dashboard'),

    # ---------------------------------------------------------
    # AUTENTICAÇÃO (SISTEMA DE ACESSO)
    # ---------------------------------------------------------
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ---------------------------------------------------------
    # CRUD - EMPRESAS (UNIDADES)
    # ---------------------------------------------------------
    # Alterado de '' para 'empresas/' para evitar conflito com o Dashboard
    path('empresas/', views.EmpresaList.as_view(), name='list_empresas'),
    path('empresa/nova/', views.EmpresaCreate.as_view(), name='create_empresa'),
    path('empresa/<int:pk>/', views.EmpresaDetail.as_view(), name='detail_empresa'),
    path('empresa/<int:pk>/editar/', views.EmpresaUpdate.as_view(), name='update_empresa'),
    path('empresa/<int:pk>/deletar/', views.EmpresaDelete.as_view(), name='delete_empresa'),

    # ---------------------------------------------------------
    # CRUD - FUNCIONÁRIOS (AGENTES)
    # ---------------------------------------------------------
    path('funcionarios/', views.FuncionarioList.as_view(), name='list_funcionarios'),
    path('funcionarios/novo/', views.FuncionarioCreate.as_view(), name='create_funcionario'),
    path('funcionarios/<int:pk>/editar/', views.FuncionarioUpdate.as_view(), name='update_funcionario'),
    path('funcionarios/<int:pk>/deletar/', views.FuncionarioDelete.as_view(), name='delete_funcionario'),

    # ---------------------------------------------------------
    # CRUD - DEPARTAMENTOS
    # ---------------------------------------------------------
    path('departamentos/', views.DepartamentoListView.as_view(), name='list_departamentos'),
    path('departamentos/novo/', views.DepartamentoCreateView.as_view(), name='create_departamento'),
    path('departamentos/editar/<int:pk>/', views.DepartamentoUpdateView.as_view(), name='update_departamento'),
    path('departamentos/deletar/<int:pk>/', views.DepartamentoDeleteView.as_view(), name='delete_departamento'),

    # ---------------------------------------------------------
    # CRUD - DOCUMENTOS
    # ---------------------------------------------------------
    path('documentos/', views.DocumentoListView.as_view(), name='list_documentos'),
    path('documentos/novo/', views.DocumentoCreateView.as_view(), name='create_documento'),
    path('documentos/<int:pk>/deletar/', views.DocumentoDeleteView.as_view(), name='delete_documento'),

    # ---------------------------------------------------------
    # CRUD - HORAS EXTRAS
    # ---------------------------------------------------------
    path('horas-extras/', views.HoraExtraListView.as_view(), name='list_horas'),
    path('horas-extras/novo/', views.HoraExtraCreateView.as_view(), name='create_hora'),
    path('horas-extras/<int:pk>/deletar/', views.HoraExtraDeleteView.as_view(), name='delete_hora'),
]