# Generated by Django 5.0.4 on 2024-05-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0021_alter_alunos_tipo_sanguineo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('4', 'B-'), ('7', 'O+'), ('0', 'Não informado'), ('8', 'O-'), ('3', 'B+'), ('6', 'AB-'), ('5', 'AB+'), ('2', 'A-'), ('1', 'A+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('5', 'Viúvo'), ('1', 'Solteiro'), ('6', 'União Estável'), ('3', 'Separado'), ('2', 'Casado'), ('4', 'Divorciado')], max_length=13, null=True),
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
            field=models.CharField(blank=True, choices=[('1', 'Nascimento'), ('3', 'Outras'), ('2', 'Casamento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('1', 'Não recebe'), ('2', 'Em hospital'), ('3', 'Em domicílio')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Transferido', 'Noturno'), ('Desistente', 'Desistente/Evasão Escolar'), ('Ativo', 'Na Turma')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Verspertino', 'Verspertino'), ('Matutino', 'Matutino'), ('Noturno', 'Noturno')], default=1, max_length=12),
        ),
    ]
