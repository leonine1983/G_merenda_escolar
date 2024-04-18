from rh.models import Vinculo_empregaticio, Escola, Contrato, Ano, Pessoas
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .professor_form import  Contrato_form


class Create_Pessoa_Aplica_Vinculo(LoginRequiredMixin, SuccessMessageMixin,  CreateView):
    model = Contrato
    form_class = Contrato_form
    template_name = 'Escola/inicio.html'
    success_url = reverse_lazy('Gestao_Escolar:GE_Escola_inicio')    
    success_message = 'Criado com sucesso'

    def get_success_url(self):
        return reverse_lazy('Gestao_Escolar:Professores_Encaminhamento', kwargs = {'pk' : self.object.id, 'destino':self.object.nome_escola.id, 'profissao': self.object.nome_profissao.id})    
    
    # Esse model recebe o Id da pessoa, o tipo de vínculo, e o ano letivo
    # Envia a query para o form ser inicializado
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs ['pessoa'] = Pessoas.objects.filter(pk = self.kwargs['pk'])
        kwargs ['ano'] = Ano.objects.filter(ano = self.kwargs['ano'])
        kwargs ['escola'] = Escola.objects.filter(pk = self.request.session['escola_id'])
        return kwargs  


    def form_valid(self, form):
        response = super().form_valid(form)
        if not self.object:
            messages.error(self.request, 'Não foi possível criar o registro.')
        else:
            messages.success(self.request, 'Criado com sucesso.')
        return response

    
    def get_context_data(self, **kwargs):
        svg = '<i class="fs-6 fa-duotone fa-person-chalkboard"></i>'
        context = super().get_context_data(**kwargs)        
        context['titulo_page'] = 'Professores | Criar Vínculo'          
        context['svg'] = svg 
        context['lista_all'] = Vinculo_empregaticio.objects.all()
        #context['now'] = datetime.now()     
        context['conteudo_page'] = "seleciona_pessoas-vinculo_contrato"       
        
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
            



            