# Generated by Django 4.2.2 on 2023-10-25 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0029_alter_vinculo_empregaticio_vinculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculo_empregaticio',
            name='vinculo',
            field=models.CharField(choices=[('decreto', 'Decreto'), ('contrato', 'Contrato'), ('efetivo', 'efetivo'), ('estagio', 'estagio')], max_length=10, null=True),
        ),
    ]
