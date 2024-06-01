# Generated by Django 5.0.4 on 2024-05-31 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0084_alter_alunos_estado_civil_alter_alunos_tipo_certidao_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='disponibilidadeprofessor',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='disponibilidadeprofessor',
            name='ano_letivo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.anoletivo'),
        ),
        migrations.AddField(
            model_name='disponibilidadeprofessor',
            name='dia_da_semana',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='disponibilidadeprofessor',
            name='horario_fim',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='disponibilidadeprofessor',
            name='horario_inicio',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('6', 'União Estável'), ('4', 'Divorciado'), ('1', 'Solteiro'), ('5', 'Viúvo'), ('2', 'Casado'), ('3', 'Separado')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('2', 'Casamento'), ('1', 'Nascimento'), ('3', 'Outras')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('0', 'Não informado'), ('6', 'AB-'), ('8', 'O-'), ('4', 'B-'), ('3', 'B+'), ('7', 'O+'), ('1', 'A+'), ('2', 'A-'), ('5', 'AB+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='disponibilidadeprofessor',
            name='periodo',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='disponibilidadeprofessor',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.profissionais'),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('2', 'Em hospital'), ('3', 'Em domicílio'), ('1', 'Não recebe')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Desistente', 'Desistente/Evasão Escolar'), ('Transferido', 'Noturno'), ('Ativo', 'Na Turma')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Noturno', 'Noturno'), ('Matutino', 'Matutino'), ('Verspertino', 'Verspertino')], default=1, max_length=12),
        ),
        migrations.RemoveField(
            model_name='disponibilidadeprofessor',
            name='dia_semana',
        ),
    ]