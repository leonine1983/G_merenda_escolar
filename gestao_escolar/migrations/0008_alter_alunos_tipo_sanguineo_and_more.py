# Generated by Django 5.0.4 on 2024-04-22 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0007_alter_alunos_tipo_sanguineo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('5', 'AB+'), ('7', 'O+'), ('6', 'AB-'), ('0', 'Não informado'), ('4', 'B-'), ('8', 'O-'), ('3', 'B+'), ('2', 'A-'), ('1', 'A+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('6', 'União Estável'), ('1', 'Solteiro'), ('2', 'Casado'), ('4', 'Divorciado'), ('3', 'Separado'), ('5', 'Viúvo')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='justificativa_falta_document',
            field=models.CharField(blank=True, choices=[('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados'), ('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)')], max_length=2, null=True, verbose_name='Justificativa da falta de documentação'),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='local_diferenciado',
            field=models.CharField(blank=True, choices=[('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados'), ('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)')], max_length=2, null=True, verbose_name='Local Diferenciado'),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('2', 'Casamento'), ('3', 'Outras'), ('1', 'Nascimento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('2', 'Em hospital'), ('1', 'Não recebe'), ('3', 'Em domicílio')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Transferido', 'Noturno'), ('Ativo', 'Na Turma'), ('Desistente', 'Desistente/Evasão Escolar')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Verspertino', 'Verspertino'), ('Noturno', 'Noturno')], default=1, max_length=12),
        ),
    ]
