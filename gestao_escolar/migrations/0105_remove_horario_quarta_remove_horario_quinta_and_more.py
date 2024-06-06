# Generated by Django 5.0.4 on 2024-06-05 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0104_horario_sabado_alter_alunos_estado_civil_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='quarta',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='quinta',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='sabado',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='segunda',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='sexta',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='terca',
        ),
        migrations.AddField(
            model_name='horario',
            name='data_fim',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='data_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('1', 'Solteiro'), ('5', 'Viúvo'), ('2', 'Casado'), ('6', 'União Estável'), ('3', 'Separado'), ('4', 'Divorciado')], max_length=13, null=True),
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
            field=models.CharField(blank=True, choices=[('3', 'Outras'), ('2', 'Casamento'), ('1', 'Nascimento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('5', 'AB+'), ('0', 'Não informado'), ('1', 'A+'), ('3', 'B+'), ('6', 'AB-'), ('4', 'B-'), ('2', 'A-'), ('7', 'O+'), ('8', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('1', 'Médio'), ('2', 'Superior')], max_length=1),
        ),
        migrations.AlterField(
            model_name='horario',
            name='turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turma_Horario_related', to='gestao_escolar.turmas'),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('1', 'Não recebe'), ('3', 'Em domicílio'), ('2', 'Em hospital')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Transferido', 'Noturno'), ('Ativo', 'Na Turma'), ('Desistente', 'Desistente/Evasão Escolar')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.CreateModel(
            name='DiasPeriodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.periodo')),
                ('quarta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quarta_prof', to='gestao_escolar.turmadisciplina')),
                ('quinta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quinta_prof', to='gestao_escolar.turmadisciplina')),
                ('sabado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sabado_prof', to='gestao_escolar.turmadisciplina')),
                ('segunda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='segunda_prof', to='gestao_escolar.turmadisciplina')),
                ('sexta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sexta_prof', to='gestao_escolar.turmadisciplina')),
                ('terca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='terca_prof', to='gestao_escolar.turmadisciplina')),
            ],
        ),
        migrations.AlterField(
            model_name='horario',
            name='periodo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='periodo_Horario_related', to='gestao_escolar.diasperiodo'),
        ),
    ]