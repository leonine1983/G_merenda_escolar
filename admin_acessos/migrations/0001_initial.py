# Generated by Django 4.2.2 on 2023-10-15 00:35

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('foto', models.ImageField(null=True, upload_to='')),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('telefone', models.CharField(max_length=20, null=True)),
                ('data_nascimento', models.DateField(null=True)),
                ('endereco', models.CharField(max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='message_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=100, verbose_name='Escreva o assunto da sua mensagem')),
                ('messagem', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('aberta', models.BooleanField(default=False)),
                ('foi_consultado', models.BooleanField(default=False)),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('exclude_msg', models.CharField(max_length=5, null=True)),
                ('remetente', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='Remetente da mensagem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_message', to=settings.AUTH_USER_MODEL, verbose_name='Pequise o nome do destinatário')),
            ],
            options={
                'ordering': ['-data_envio'],
            },
        ),
    ]
