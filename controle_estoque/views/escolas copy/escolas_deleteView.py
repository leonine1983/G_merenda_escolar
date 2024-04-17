from Controle_Estoque.models import Escolas_model
from django.views.generic import DeleteView
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy




class Escolas_DeleteView(DeleteView):
    model = Escolas_model
    template_name = 'Controle_Estoque/escolas/escola_cadastro.html'
    success_url =  reverse_lazy('Controle_Estoque:escola_lista')

    def get_context_data(self, **kwargs):
        dados = Escolas_model.objects.filter(pk=self.kwargs['pk'])
        for d in dados:
            dados = d.nome_escola
        svg = '<svg class="bi" width="30" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M337.8 5.4C327-1.8 313-1.8 302.2 5.4L166.3 96H48C21.5 96 0 117.5 0 144V464c0 26.5 21.5 48 48 48H592c26.5 0 48-21.5 48-48V144c0-26.5-21.5-48-48-48H473.7L337.8 5.4zM256 416c0-35.3 28.7-64 64-64s64 28.7 64 64v96H256V416zM96 192h32c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H96c-8.8 0-16-7.2-16-16V208c0-8.8 7.2-16 16-16zm400 16c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H512c-8.8 0-16-7.2-16-16V208zM96 320h32c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H96c-8.8 0-16-7.2-16-16V336c0-8.8 7.2-16 16-16zm400 16c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H512c-8.8 0-16-7.2-16-16V336zM232 176a88 88 0 1 1 176 0 88 88 0 1 1 -176 0zm88-48c-8.8 0-16 7.2-16 16v32c0 8.8 7.2 16 16 16h32c8.8 0 16-7.2 16-16s-7.2-16-16-16H336V144c0-8.8-7.2-16-16-16z"></path></svg>'
        context = super().get_context_data(**kwargs)
        context["svg"] = mark_safe(svg)        
        context["title"] = 'Delete Escola ou Departamento'        
        context ['active'] = 'escolas'
        context ['class_active'] = 'escolasCreate'
        context ['fornecedor'] = 'cadastro'        
        context ['delete'] = 'delete'
        context ['object_list'] = dados
        return context