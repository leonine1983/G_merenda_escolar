# Generated by Django 5.0.4 on 2024-04-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0011_alter_alunos_tipo_sanguineo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('6', 'AB-'), ('1', 'A+'), ('3', 'B+'), ('2', 'A-'), ('5', 'AB+'), ('4', 'B-'), ('7', 'O+'), ('0', 'Não informado'), ('8', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('1', 'Solteiro'), ('4', 'Divorciado'), ('6', 'União Estável'), ('2', 'Casado'), ('3', 'Separado'), ('5', 'Viúvo')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('1', 'Nascimento'), ('3', 'Outras'), ('2', 'Casamento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('2', 'Em hospital'), ('3', 'Em domicílio'), ('1', 'Não recebe')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Transferido', 'Noturno'), ('Ativo', 'Na Turma'), ('Desistente', 'Desistente/Evasão Escolar')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Noturno', 'Noturno'), ('Verspertino', 'Verspertino')], default=1, max_length=12),
        ),
    ]