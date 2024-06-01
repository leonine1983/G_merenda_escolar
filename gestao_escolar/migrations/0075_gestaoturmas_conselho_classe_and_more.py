# Generated by Django 5.0.4 on 2024-05-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0074_trimestre_final_alter_alunos_estado_civil_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestaoturmas',
            name='conselho_classe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='gestaoturmas',
            name='faltas_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gestaoturmas',
            name='media_final',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='gestaoturmas',
            name='recuperacao_final',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('6', 'União Estável'), ('2', 'Casado'), ('1', 'Solteiro'), ('5', 'Viúvo'), ('3', 'Separado'), ('4', 'Divorciado')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='justificativa_falta_document',
            field=models.CharField(blank=True, choices=[('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)'), ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados')], max_length=2, null=True, verbose_name='Justificativa da falta de documentação'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='local_diferenciado',
            field=models.CharField(blank=True, choices=[('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)'), ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados')], max_length=2, null=True, verbose_name='Local Diferenciado'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('2', 'Casamento'), ('1', 'Nascimento'), ('3', 'Outras')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('7', 'O+'), ('5', 'AB+'), ('2', 'A-'), ('8', 'O-'), ('4', 'B-'), ('0', 'Não informado'), ('3', 'B+'), ('6', 'AB-'), ('1', 'A+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('2', 'Em hospital'), ('1', 'Não recebe'), ('3', 'Em domicílio')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Ativo', 'Na Turma'), ('Desistente', 'Desistente/Evasão Escolar'), ('Transferido', 'Noturno')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Verspertino', 'Verspertino'), ('Noturno', 'Noturno')], default=1, max_length=12),
        ),
    ]