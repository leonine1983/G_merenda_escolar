from gestao_escolar.models import Alunos, Alunos_Documentacao
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from datetime import datetime, date
from django.urls import reverse_lazy
from gestao_escolar.views.alunos.alunos_form import Aluno_documento_form


class Upadate_Alunos_Document(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Alunos_Documentacao
    form_class = Aluno_documento_form
    #form_class = Turma_form
    template_name = 'Escola/inicio.html'
    success_message = "Aluno registrado com sucesso!!"

    def get_success_url(self):
        aluno_id = self.object.id 
        return reverse_lazy('Gestao_Escolar:alunos_perfil', kwargs={'pk': aluno_id})  

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Assuming you have a view where you pass 'pk' in the URL conf
        pk = self.kwargs.get('pk')
        print(f'esse eo vlaor {pk}')
        if pk is not None:
            # Correct way to filter Alunos
            kwargs['aluno_create'] = Alunos.objects.filter(aluno_documento_related__aluno__pk=pk).first()
            print(f'esse eo vlaor {kwargs['aluno_create']}')
        return kwargs

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)        
        context['titulo_page'] = 'Alunos'                  
        context['Alunos'] = Alunos.objects.all()
        context['now'] = datetime.now()
        context['conteudo_page'] = 'Registrar Alunos Documento'      
        
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
