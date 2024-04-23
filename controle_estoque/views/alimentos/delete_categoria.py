from controle_estoque.models import Categoria_alimentos
from django.views.generic import DeleteView
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy


class Categoria_DeleteView(DeleteView):
    model = Categoria_alimentos
    template_name = 'controle_estoque/alimentos/alimentos_cadastro.html'
    success_url = reverse_lazy ('controle_estoque:categoria_lista')

    def get_context_data(self, **kwargs):
        delete = Categoria_alimentos.objects.filter(pk = self.kwargs['pk'])
        for d in delete:
            dados = d.nome

        svg = '<svg xmlns="http://www.w3.org/2000/svg" class="bi" width="30" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M192 0c-41.8 0-77.4 26.7-90.5 64H64C28.7 64 0 92.7 0 128V448c0 35.3 28.7 64 64 64H320c35.3 0 64-28.7 64-64V128c0-35.3-28.7-64-64-64H282.5C269.4 26.7 233.8 0 192 0zm0 64a32 32 0 1 1 0 64 32 32 0 1 1 0-64zM72 272a24 24 0 1 1 48 0 24 24 0 1 1 -48 0zm104-16H304c8.8 0 16 7.2 16 16s-7.2 16-16 16H176c-8.8 0-16-7.2-16-16s7.2-16 16-16zM72 368a24 24 0 1 1 48 0 24 24 0 1 1 -48 0zm88 0c0-8.8 7.2-16 16-16H304c8.8 0 16 7.2 16 16s-7.2 16-16 16H176c-8.8 0-16-7.2-16-16z"/></svg>'
        context = super().get_context_data(**kwargs)
        context["svg"] = mark_safe(svg)
        context["title"] = "Deleta categoria"
        context['active'] = "categoria"
        context['delete'] = "Deseja deletar a categoria "
        context['object_list'] = dados

        
        

        return context  
