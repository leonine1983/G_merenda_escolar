# Generated by Django 5.0.4 on 2024-06-01 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estoque', '0059_alter_movimentacao_estoque_unidademedida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao_estoque',
            name='unidadeMedida',
            field=models.CharField(choices=[('kg', 'kg'), ('litros', 'litros')], max_length=10, verbose_name='Unidade de Medida'),
        ),
    ]
