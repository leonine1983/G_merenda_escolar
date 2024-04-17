from RH.models import Pessoas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView
from .pessoas_form import Pessoas_form
from django.urls import reverse_lazy


class Pessoas_deleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Pessoas
    #fields = '__all__'
    template_name = 'rh/inicio.html'
    success_url = reverse_lazy('RH:Pessoas_createView')
    success_message = 'Pessoa Deletada com sucesso!!'

    def get_context_data(self, **kwargs):
        svg = '<svg xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M38-160v-94q0-35 18-63.5t50-42.5q73-32 131.5-46T358-420q62 0 120 14t131 46q32 14 50.5 42.5T678-254v94H38Zm700 0v-94q0-63-32-103.5T622-423q69 8 130 23.5t99 35.5q33 19 52 47t19 63v94H738ZM358-481q-66 0-108-42t-42-108q0-66 42-108t108-42q66 0 108 42t42 108q0 66-42 108t-108 42Zm360-150q0 66-42 108t-108 42q-11 0-24.5-1.5T519-488q24-25 36.5-61.5T568-631q0-45-12.5-79.5T519-774q11-3 24.5-5t24.5-2q66 0 108 42t42 108ZM98-220h520v-34q0-16-9.5-31T585-306q-72-32-121-43t-106-11q-57 0-106.5 11T130-306q-14 6-23 21t-9 31v34Zm260-321q39 0 64.5-25.5T448-631q0-39-25.5-64.5T358-721q-39 0-64.5 25.5T268-631q0 39 25.5 64.5T358-541Zm0 321Zm0-411Z"/></svg>'
        context = super().get_context_data(**kwargs)        
        context['titulo_page'] = 'Pessoas'          
        context['svg'] = svg        
        nome_instacia = self.get_object()  
        context['nome_instancia'] = nome_instacia.nome
        context['conteudo_page'] = 'Deleta pessoas do Sistema'        
        context['lista_pessoas'] = Pessoas.objects.all()[:10]


        return context


 

