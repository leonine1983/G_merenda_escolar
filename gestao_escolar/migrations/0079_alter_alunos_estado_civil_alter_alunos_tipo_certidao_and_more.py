# Generated by Django 5.0.4 on 2024-05-30 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0078_alter_alunos_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('2', 'Casado'), ('4', 'Divorciado'), ('1', 'Solteiro'), ('5', 'Viúvo'), ('6', 'União Estável'), ('3', 'Separado')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('2', 'Casamento'), ('1', 'Nascimento'), ('3', 'Outras')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('4', 'B-'), ('0', 'Não informado'), ('5', 'AB+'), ('8', 'O-'), ('6', 'AB-'), ('3', 'B+'), ('2', 'A-'), ('1', 'A+'), ('7', 'O+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Transferido', 'Noturno'), ('Desistente', 'Desistente/Evasão Escolar'), ('Ativo', 'Na Turma')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Verspertino', 'Verspertino'), ('Noturno', 'Noturno'), ('Matutino', 'Matutino')], default=1, max_length=12),
        ),
        migrations.CreateModel(
            name='HorarioAula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.IntegerField(choices=[(1, 'Segunda-feira'), (2, 'Terça-feira'), (3, 'Quarta-feira'), (4, 'Quinta-feira'), (5, 'Sexta-feira')])),
                ('periodo', models.IntegerField(choices=[(1, '1º período'), (2, '2º período'), (3, '3º período')])),
                ('sequencia_didatica', models.TextField(blank=True, null=True)),
                ('turma_disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.turmadisciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Falta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.matriculas')),
                ('horario_aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.horarioaula')),
            ],
        ),
    ]
