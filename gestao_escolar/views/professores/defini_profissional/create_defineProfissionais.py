from rh.models import Pessoas, Encaminhamentos, Ano, Contrato
from gestao_escolar.models import AnoLetivo, Profissionais, Cargo
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .create_defineProfissionais_FORM import Form_defineProfissionais


class Create_Define_Profissional(LoginRequiredMixin, CreateView):
    model = Profissionais
    #fields = '__all__'
    form_class = Form_defineProfissionais
    template_name = 'Escola/inicio.html'
    success_url = reverse_lazy('Gestao_Escolar:GE_Escola_inicio')    

    def get_success_url(self):
        return reverse_lazy('Gestao_Escolar:Professores_Profissionais_create')
    

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()  
        escola = self.request.session['escola_id']  
        profissionais_list = Profissionais.objects.values_list('nome__id', flat=True)
        encaminhamento_esc = Encaminhamentos.objects.filter(destino = escola, encaminhamento__ano_contrato__anoletivo = self.request.session['anoLetivo_id'] )
        kwargs['nome_query'] = encaminhamento_esc.exclude(id__in = profissionais_list )
        return kwargs
    
    def get_context_data(self, **kwargs):
        escola = self.request.session['escola_id']
        svg = '<i class="fs-6 fa-duotone fa-person-chalkboard"></i>'
        context = super().get_context_data(**kwargs)        
        context['titulo_page'] = 'Professores'          
        context['svg'] = svg 

        
        context['lista_all'] = Profissionais.objects.filter(nome__destino = escola, nome__encaminhamento__ano_contrato__anoletivo = self.request.session['anoLetivo_id'] )       
        context['cargo_all'] = Cargo.objects.all()
       
        context['conteudo_page'] = "cargos/funcionarios"       
        
        context['page_ajuda'] = "<div class='m-2'><b>Nessa área, definimos todos os dados para a celebração do contrato com o profissional. </b>\
            <hr>\
                <div class='border bg-secondary p-2'>\
                    <h2>Pessoar a ser contratada</h2>\
                    <p>Espaço onde é selecionado no nome da pessoa que será contratada. Se por alguma razão estiver vazio, clique aqui: <a class='btn btn-sm btn-primary' href='pessoas/create/'>Clique aqui para cadastrar uma pessoa no sistema</a></p>\
                </div>\
                <div class=' p-2'>\
                    <p><h2>Ano de contrato</h2>\
                    <p>Espaço onde é selecionado o ano em que o profissional será contratado. Se por alguma razão estiver vazio, clique aqui: <a class='btn btn-sm btn-secondary' href='ano/create/'>Clique aqui para cadastrar um ANO no sistema</a></p>\
                </div>\
                <div class='border bg-secondary p-2'>\
                    <p><h2>Tipo de contrato</h2>\
                    <p>Espaço onde é selecionado o modelo de contrato que será utilizado para a contratação. Se estiver vazio,  clique aqui: <a class='btn btn-sm btn-primary' href='ano/create/'>Clique aqui para criar um MODELO DE CONTRATO no sistema</a></p>\
                </div>\
                <div class=' p-2'>\
                    <p><h2>Função que irá desempenhar na escola</h2>\
                    <p>Local em que é definido a função pela qual o profissional está sendo contratado</p>\
                </div>\
                <div class='border bg-secondary p-2'>\
                    <p><h2>Escola onde o profissional irá desempenhar suas funções</h2>\
                    <p>Espaço onde é selecionado a instituição que o profissional desempenhará suas funções. Se estiver vazio,  clique aqui: <a class='btn btn-sm btn-primary' href='escola/create/'>Clique aqui para Adicionar uma Escola</a></p>\
                </div>"
        
        return context
            



            