# Generated by Django 4.2.2 on 2023-10-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0019_alter_encaminhamentos_destino_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculo_empregaticio',
            name='vinculo',
            field=models.CharField(choices=[('decreto', 'Decreto'), ('contrato', 'Contrato'), ('estagio', 'estagio'), ('efetivo', 'efetivo')], max_length=10, null=True),
        ),
    ]
