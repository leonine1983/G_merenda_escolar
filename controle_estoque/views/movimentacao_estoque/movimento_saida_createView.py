from typing import Any, Dict, Optional, Type
from django.forms.models import BaseModelForm
from controle_estoque.models import Movimentacao_Estoque
from .movimento_form import Movimento_Saida_Form
from django.views.generic import CreateView
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy




class MovimentoEstoque_Saida_CreateView(CreateView):
    model = Movimentacao_Estoque
    form_class = Movimento_Saida_Form
    template_name = 'Controle_Estoque/movimentacao_estoque/movi_cadastro.html'
    success_url =  reverse_lazy('Controle_Estoque:movi_estoque_CreateVies')

    def get_context_data(self, **kwargs):
        svg = '<svg class="bi" width="30" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M0 48C0 21.5 21.5 0 48 0H368c26.5 0 48 21.5 48 48V96h50.7c17 0 33.3 6.7 45.3 18.7L589.3 192c12 12 18.7 28.3 18.7 45.3V256v32 64c17.7 0 32 14.3 32 32s-14.3 32-32 32H576c0 53-43 96-96 96s-96-43-96-96H256c0 53-43 96-96 96s-96-43-96-96H48c-26.5 0-48-21.5-48-48V48zM416 256H544V237.3L466.7 160H416v96zM160 464a48 48 0 1 0 0-96 48 48 0 1 0 0 96zm368-48a48 48 0 1 0 -96 0 48 48 0 1 0 96 0zM257 95c-9.4-9.4-24.6-9.4-33.9 0s-9.4 24.6 0 33.9l39 39H96c-13.3 0-24 10.7-24 24s10.7 24 24 24H262.1l-39 39c-9.4 9.4-9.4 24.6 0 33.9s24.6 9.4 33.9 0l80-80c9.4-9.4 9.4-24.6 0-33.9L257 95z"></path></svg>'
        context = super().get_context_data(**kwargs)
        context["svg"] = mark_safe(svg)
        context["title"] = 'Envio de Gêneros às Escolas ou Outros Departamentos'
        context ['class_active'] = 'envio às Escolas'
        context ['active'] = 'envio às Escolas'
        context ['fornecedor'] = 'cadastro'
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs