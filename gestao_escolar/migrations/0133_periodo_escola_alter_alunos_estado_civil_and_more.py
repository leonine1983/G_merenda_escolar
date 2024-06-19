# Generated by Django 5.0.4 on 2024-06-12 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0132_remove_horario_sabado_alter_alunos_estado_civil_and_more'),
        ('rh', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='escola',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rh.escola'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('5', 'Viúvo'), ('4', 'Divorciado'), ('1', 'Solteiro'), ('2', 'Casado'), ('3', 'Separado'), ('6', 'União Estável')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='justificativa_falta_document',
            field=models.CharField(blank=True, choices=[('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados'), ('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)')], max_length=2, null=True, verbose_name='Justificativa da falta de documentação'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='local_diferenciado',
            field=models.CharField(blank=True, choices=[('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados'), ('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)')], max_length=2, null=True, verbose_name='Local Diferenciado'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('2', 'A-'), ('6', 'AB-'), ('8', 'O-'), ('4', 'B-'), ('0', 'Não informado'), ('1', 'A+'), ('3', 'B+'), ('7', 'O+'), ('5', 'AB+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('2', 'Superior'), ('1', 'Médio')], max_length=1),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('2', 'Em hospital'), ('1', 'Não recebe'), ('3', 'Em domicílio')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Noturno', 'Noturno'), ('Verspertino', 'Verspertino'), ('Matutino', 'Matutino')], default=1, max_length=12),
        ),
    ]