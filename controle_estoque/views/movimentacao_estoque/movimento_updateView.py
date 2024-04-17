from controle_estoque.models import Movimentacao_Estoque
from django.utils.safestring import mark_safe
from django.views.generic import UpdateView
from django.urls import reverse_lazy




class MovimentoEstoque_updateView(UpdateView):
    model = Movimentacao_Estoque
    fields = '__all__'
    template_name = 'Controle_Estoque/movimentacao_estoque/movi_cadastro.html'
    success_url =  reverse_lazy('Controle_Estoque:movi_estoque_listaView')

    def get_context_data(self, **kwargs):
        svg = '<svg class="bi" width="30" height="24" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path d="M36.8 192H603.2c20.3 0 36.8-16.5 36.8-36.8c0-7.3-2.2-14.4-6.2-20.4L558.2 21.4C549.3 8 534.4 0 518.3 0H121.7c-16 0-31 8-39.9 21.4L6.2 134.7c-4 6.1-6.2 13.2-6.2 20.4C0 175.5 16.5 192 36.8 192zM64 224V384v80c0 26.5 21.5 48 48 48H336c26.5 0 48-21.5 48-48V384 224H320V384H128V224H64zm448 0V480c0 17.7 14.3 32 32 32s32-14.3 32-32V224H512z"/></svg>'
        context = super().get_context_data(**kwargs)
        context["svg"] = mark_safe(svg)
        context["title"] = 'Atualização de Gêneros Alimentícios no Depósito Central'
        context ['class_active'] = 'create Deposito Central'
        context ['active'] = 'Deposito Central'
        context ['fornecedor'] = 'cadastro'
        
        return context




         