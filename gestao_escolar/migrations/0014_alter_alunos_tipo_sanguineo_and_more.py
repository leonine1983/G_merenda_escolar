# Generated by Django 5.0.4 on 2024-04-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0013_alter_alunos_tipo_sanguineo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('2', 'A-'), ('3', 'B+'), ('1', 'A+'), ('4', 'B-'), ('8', 'O-'), ('7', 'O+'), ('0', 'Não informado'), ('6', 'AB-'), ('5', 'AB+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('4', 'Divorciado'), ('6', 'União Estável'), ('3', 'Separado'), ('5', 'Viúvo'), ('1', 'Solteiro'), ('2', 'Casado')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='justificativa_falta_document',
            field=models.CharField(blank=True, choices=[('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)'), ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados')], max_length=2, null=True, verbose_name='Justificativa da falta de documentação'),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='local_diferenciado',
            field=models.CharField(blank=True, choices=[('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)'), ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados')], max_length=2, null=True, verbose_name='Local Diferenciado'),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('1', 'Nascimento'), ('2', 'Casamento'), ('3', 'Outras')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('1', 'Médio'), ('2', 'Superior')], max_length=1),
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
            field=models.CharField(choices=[('Noturno', 'Noturno'), ('Matutino', 'Matutino'), ('Verspertino', 'Verspertino')], default=1, max_length=12),
        ),
    ]
