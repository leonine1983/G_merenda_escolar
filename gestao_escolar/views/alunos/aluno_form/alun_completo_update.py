
from django import forms
from django.utils.safestring import mark_safe
from rh.models import Sexo
from gestao_escolar.models import (Alunos, Etnia, Nacionalidade,
                                     Pais_origem, Deficiencia_aluno)


choices = {
    ('1','A+'),
    ('2','A-'),
    ('3','B+'),
    ('4','B-'),
    ('5','AB+'),
    ('6','AB-'),
    ('7','O+'),
    ('8','O-'),    
    ('0','Não informado')
}


class Alunos_atualiza(forms.ModelForm):

    nome_social = forms.CharField(
        label='Nome Social (Se possuir):',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )   
    data_nascimento = forms.DateField(
        label='Data de Nascimento:',
        widget=forms.DateInput(attrs={'class': 'form-control border border-info p-3 pb-3  text-info col2 m-2 rounded-1', 'type': 'date'}),        
    )
    
    sexo = forms.ModelChoiceField(
        label='Sexo:',
        queryset=Sexo.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    )
    
    etnia = forms.ModelChoiceField(
        queryset=Etnia.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    )
    tel_celular_aluno = forms.CharField(   
        label=mark_safe('<i class="fa-brands fa-whatsapp text-success"></i> Telefone celular do aluno'),   
        widget=forms.TextInput(attrs={'class': 'form-control  border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=True
    )
    email = forms.CharField(        
        widget=forms.EmailInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
   
    tel_celular_mae = forms.CharField(  
        label=mark_safe('<i class="fa-brands fa-whatsapp text-success"></i> Telefone celular da mãe'),      
        widget=forms.TextInput(attrs={'class': 'form-control  border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    nome_pai = forms.CharField(        
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    
    tel_celular_pai = forms.CharField(      
        label=mark_safe('<i class="fa-brands fa-whatsapp text-success"></i> Telefone celular do pai'),    
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    naturalidade = forms.CharField(        
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
    )
    nacionalidade = forms.ModelChoiceField(
        queryset=Nacionalidade.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    )
    """
    nacionalidade = forms.ModelChoiceField(
        queryset=Nacionalidade.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    )
    pais_origem = forms.ModelChoiceField(
        queryset=Pais_origem.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    data_entrada_no_pais = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col2 m-2 rounded-1', 'type': 'date'}),      
        required=False  
    )
    documento_estrangeiro = forms.CharField(        
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    deficiencia_aluno = forms.ModelChoiceField(
        queryset=Deficiencia_aluno.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    )
    tipo_sanguineo = forms.ChoiceField(
    choices=choices,
    widget=forms.Select(attrs={'class': ' border border-info p-2 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False
    )

    beneficiario_aux_Brasil = forms.BooleanField(   
    label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
    widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False        
    )

    necessita_edu_especial = forms.BooleanField(   
    label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
    widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False        
    )
    
    sindrome_de_Down = forms.BooleanField(   
    label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
    widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False        
    )
    quilombola = forms.BooleanField(   
    label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
    widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False        
    )
    irmao_gemeo  = forms.BooleanField(   
    label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
    widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False        
    )
    vacina_covid_19  = forms.BooleanField(   
        label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
        widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
        required=False        
    )
    dose_vacina_covid_19 = forms.IntegerField(        
        widget=forms.NumberInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    ) 
    """
    class Meta:
        model = Alunos
        fields = '__all__'
        exclude = ['idade', 
                   'aluno_inativo', 'nome_completo', 'pais_origem', 'data_entrada_no_pais', 
                       'documento_estrangeiro', 'deficiencia_aluno', 'tipo_sanguineo', 
                       'beneficiario_aux_Brasil', 'necessita_edu_especial', 'sindrome_de_Down', 
                       'quilombola', 'irmao_gemeo', 'vacina_covid_19', 'dose_vacina_covid_19', 'res_cadastro', 'res_atualiza_cadastro' ]