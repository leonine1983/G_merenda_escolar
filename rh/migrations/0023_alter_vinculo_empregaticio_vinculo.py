# Generated by Django 4.2.2 on 2023-10-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0022_alter_vinculo_empregaticio_vinculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculo_empregaticio',
            name='vinculo',
            field=models.CharField(choices=[('estagio', 'estagio'), ('contrato', 'Contrato'), ('decreto', 'Decreto'), ('efetivo', 'efetivo')], max_length=10, null=True),
        ),
    ]
