# Generated by Django 5.0.4 on 2024-05-21 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0050_alter_alunos_estado_civil_and_more'),
        ('rh', '__first__'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='RG_UF',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rh.uf_unidade_federativa'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('1', 'Solteiro'), ('3', 'Separado'), ('5', 'Viúvo'), ('6', 'União Estável'), ('4', 'Divorciado'), ('2', 'Casado')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('3', 'Outras'), ('2', 'Casamento'), ('1', 'Nascimento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('6', 'AB-'), ('0', 'Não informado'), ('1', 'A+'), ('3', 'B+'), ('7', 'O+'), ('2', 'A-'), ('8', 'O-'), ('5', 'AB+'), ('4', 'B-')], max_length=3, null=True),
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
    ]