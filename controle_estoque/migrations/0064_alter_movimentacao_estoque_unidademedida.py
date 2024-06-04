# Generated by Django 5.0.4 on 2024-06-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estoque', '0063_alter_movimentacao_estoque_unidademedida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao_estoque',
            name='unidadeMedida',
            field=models.CharField(choices=[('kg', 'kg'), ('litros', 'litros')], max_length=10, verbose_name='Unidade de Medida'),
        ),
    ]
