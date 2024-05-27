# Generated by Django 5.0.4 on 2024-05-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0061_alter_alunos_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('2', 'Casado'), ('1', 'Solteiro'), ('4', 'Divorciado'), ('3', 'Separado'), ('5', 'Viúvo'), ('6', 'União Estável')], max_length=13, null=True),
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
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('2', 'Casamento'), ('3', 'Outras'), ('1', 'Nascimento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('3', 'B+'), ('0', 'Não informado'), ('2', 'A-'), ('7', 'O+'), ('5', 'AB+'), ('1', 'A+'), ('6', 'AB-'), ('8', 'O-'), ('4', 'B-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('3', 'Em domicílio'), ('1', 'Não recebe'), ('2', 'Em hospital')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Transferido', 'Noturno'), ('Ativo', 'Na Turma'), ('Desistente', 'Desistente/Evasão Escolar')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Verspertino', 'Verspertino'), ('Matutino', 'Matutino'), ('Noturno', 'Noturno')], default=1, max_length=12),
        ),
    ]
