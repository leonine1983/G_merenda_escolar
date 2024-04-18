from django.forms.models import BaseModelForm
from django.http import HttpResponse
from rh.models import Vinculo_empregaticio, Pessoas, Encaminhamentos, Contrato, Profissao
from gestao_escolar.models import Escola
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .professor_form import Create_Pessoa_Encaminhamento_form
from django.http import HttpResponseRedirect

 
class Create_Pessoa_Encaminhamento(LoginRequiredMixin, CreateView):
    model = Encaminhamentos
    # fields = '__all__'
    form_class = Create_Pessoa_Encaminhamento_form
    template_name = 'Escola/inicio.html'
    success_url = reverse_lazy('Gestao_Escolar:GE_Escola_inicio')    

    # Recebe o Id vindo pela url para inicializar o select no form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs() 
        kwargs['encaminhamento'] = Contrato.objects.filter(pk=self.kwargs['pk'])  
        kwargs['destino'] = Escola.objects.filter(pk=self.kwargs['destino'])
        kwargs['profissao'] = Profissao.objects.filter(pk=self.kwargs['profissao'])
       

        # Verifica se os filtros retornaram resultados
        if not kwargs['encaminhamento']:
            kwargs['encaminhamento'] = Contrato.objects.none()
        if not kwargs['destino']:
            kwargs['destino'] = Escola.objects.none()
        if not kwargs['profissao']:
            kwargs['profissao'] = Profissao.objects.none()

        return kwargs  
    
    # Salva automaticamente os dado se o form for válido
    def form_valid(self, form) :
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())  
    

    def get_context_data(self, **kwargs):
        svg = '<i class="fs-6 fa-duotone fa-person-chalkboard"></i>'
        context = super().get_context_data(**kwargs)        
        context['titulo_page'] = 'Professores | Criar Vínculo'          
        context['svg'] = svg 
        context['lista_all'] = Vinculo_empregaticio.objects.all()
        #context['now'] = datetime.now()     
        context['conteudo_page'] = "Professores-Pessoas-Vinculo"       
        
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
            



            