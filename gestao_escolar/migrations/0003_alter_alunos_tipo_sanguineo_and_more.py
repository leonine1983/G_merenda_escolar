# Generated by Django 5.0.4 on 2024-04-22 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0002_alter_alunos_tipo_sanguineo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('7', 'O+'), ('3', 'B+'), ('0', 'Não informado'), ('2', 'A-'), ('5', 'AB+'), ('8', 'O-'), ('1', 'A+'), ('4', 'B-'), ('6', 'AB-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('2', 'Casado'), ('3', 'Separado'), ('6', 'União Estável'), ('5', 'Viúvo'), ('4', 'Divorciado'), ('1', 'Solteiro')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('1', 'Nascimento'), ('3', 'Outras'), ('2', 'Casamento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Verspertino', 'Verspertino'), ('Matutino', 'Matutino'), ('Noturno', 'Noturno')], default=1, max_length=12),
        ),
    ]