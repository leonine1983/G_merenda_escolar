# Generated by Django 4.2.2 on 2023-11-02 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0052_alter_vinculo_empregaticio_vinculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculo_empregaticio',
            name='vinculo',
            field=models.CharField(choices=[('efetivo', 'efetivo'), ('decreto', 'Decreto'), ('contrato', 'Contrato'), ('estagio', 'estagio')], max_length=10, null=True),
        ),
    ]
