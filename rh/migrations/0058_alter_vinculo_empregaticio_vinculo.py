# Generated by Django 4.2.2 on 2023-11-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0057_alter_vinculo_empregaticio_vinculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculo_empregaticio',
            name='vinculo',
            field=models.CharField(choices=[('contrato', 'Contrato'), ('efetivo', 'efetivo'), ('estagio', 'estagio'), ('decreto', 'Decreto')], max_length=10, null=True),
        ),
    ]
