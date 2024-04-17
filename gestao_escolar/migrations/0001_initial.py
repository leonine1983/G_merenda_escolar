# Generated by Django 5.0.4 on 2024-04-17 17:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(default='Nome completo do aluno', max_length=120, verbose_name='Nome completo do aluno*')),
                ('nome_social', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento*')),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('tel_celular_aluno', models.CharField(default='Celular 01', max_length=30, verbose_name='Nº de telefone do aluno*')),
                ('email', models.EmailField(max_length=200, verbose_name='Email*')),
                ('nome_mae', models.CharField(default='Nome completo da Mãe', max_length=120, verbose_name='Nome da Mãe*')),
                ('tel_celular_mae', models.CharField(default='Telefone da mae', max_length=30, null=True, verbose_name='Nº do celular do mãe*')),
                ('nome_pai', models.CharField(default='Nome completo da Pai', max_length=120, null=True)),
                ('tel_celular_pai', models.CharField(default='Telefone do pai', max_length=30, null=True)),
                ('naturalidade', models.CharField(default='Cidade onde nasceu', max_length=30)),
                ('data_entrada_no_pais', models.DateField(blank=True, null=True)),
                ('documento_estrangeiro', models.CharField(blank=True, max_length=30, null=True)),
                ('tipo_sanguineo', models.CharField(choices=[('3', 'B+'), ('5', 'AB+'), ('8', 'O-'), ('1', 'A+'), ('2', 'A-'), ('6', 'AB-'), ('4', 'B-'), ('0', 'Não informado'), ('7', 'O+')], max_length=3, null=True)),
                ('beneficiario_aux_Brasil', models.BooleanField(default=False, null=True, verbose_name='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil')),
                ('necessita_edu_especial', models.BooleanField(default=False, null=True, verbose_name='Selecione se o aluno precisa de algum atendimento especial')),
                ('sindrome_de_Down', models.BooleanField(default=False, null=True, verbose_name='Selecione se o aluno for portador de Síndrome de Down')),
                ('quilombola', models.BooleanField(default=False, null=True, verbose_name='Selecione se o aluno possui deficiência')),
                ('irmao_gemeo', models.BooleanField(default=False, null=True, verbose_name='Selecione se o aluno possui irmão(s) gêmeos')),
                ('vacina_covid_19', models.BooleanField(default=False, null=True, verbose_name='Selecione se o aluno tomou vacina contra a covid 19')),
                ('dose_vacina_covid_19', models.IntegerField(blank=True, null=True, verbose_name='Preencha se o aluno tomou alguma dose da covid 19')),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Compatibilidade_EducaCenso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('nivel', models.CharField(choices=[('2', 'Superior'), ('1', 'Médio')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Deficiencia_aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ordem_historico', models.FloatField(null=True)),
                ('n_A', models.BooleanField(default=False, null=True, verbose_name='Destacar como N/S (Não avaliado) nos impressos')),
                ('faltas', models.BooleanField(default=False, null=True, verbose_name='Não permitir lançamento de faltas')),
                ('notas', models.BooleanField(default=False, null=True, verbose_name='Não permitir lançamento de notas')),
                ('historico_escolar', models.BooleanField(default=False, null=True, verbose_name='Não mostrar no histórico escolar')),
                ('papeletas', models.BooleanField(default=False, null=True, verbose_name='Não mostrar em papeletas')),
                ('ata_final', models.BooleanField(default=False, null=True, verbose_name='Não mostrar em Atas Finais')),
            ],
            options={
                'ordering': ['ordem_historico'],
            },
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Faculdades_ou_Escolas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GrauEscolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Grau/Nível Escolar')),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pais_origem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Remanejamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Desistente', 'Desistente/Evasão Escolar'), ('Ativo', 'Na Turma'), ('Transferido', 'Noturno')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento')),
                ('description', models.TextField(max_length=500, verbose_name='Descreva o motivo do Remanejamento. Ex.: Escola para onde o aluno será remanejado e o porquê.')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alunos_Documentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RG', models.CharField(blank=True, default='000.000.00-00', max_length=14, null=True)),
                ('RG_emissao', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('orgao_emissor', models.CharField(blank=True, max_length=5, null=True)),
                ('renda_familiar', models.CharField(blank=True, max_length=7, null=True)),
                ('situacao_familiar', models.CharField(blank=True, max_length=15, null=True)),
                ('CPF', models.CharField(blank=True, default='000.000.000-00', max_length=14, null=True)),
                ('login_aluno', models.CharField(blank=True, max_length=10, null=True)),
                ('senha', models.CharField(blank=True, default='12345678', max_length=10, null=True)),
                ('cartao_nacional_saude_cns', models.CharField(blank=True, max_length=20, null=True)),
                ('nis', models.CharField(blank=True, max_length=20, null=True)),
                ('inep', models.CharField(blank=True, max_length=15, null=True)),
                ('estado_civil', models.CharField(blank=True, choices=[('6', 'União Estável'), ('4', 'Divorciado'), ('5', 'Viúvo'), ('1', 'Solteiro'), ('3', 'Separado'), ('2', 'Casado')], max_length=13, null=True)),
                ('tipo_certidao', models.CharField(blank=True, choices=[('2', 'Casamento'), ('3', 'Outras'), ('1', 'Nascimento')], max_length=13, null=True)),
                ('numero_certidao', models.CharField(blank=True, max_length=15, null=True, verbose_name='Certidão de Nascimento (Matrícula Única)')),
                ('livro', models.CharField(blank=True, max_length=10, null=True)),
                ('folha', models.CharField(blank=True, max_length=10, null=True)),
                ('termo', models.CharField(blank=True, max_length=10, null=True)),
                ('emissao', models.DateField(blank=True, null=True)),
                ('distrito_certidao', models.CharField(blank=True, max_length=20, null=True)),
                ('cartorio', models.CharField(blank=True, max_length=100, null=True)),
                ('comarca', models.CharField(blank=True, max_length=100, null=True)),
                ('justificativa_falta_document', models.CharField(blank=True, choices=[('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)'), ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados')], max_length=2, null=True, verbose_name='Justificativa da falta de documentação')),
                ('local_diferenciado', models.CharField(blank=True, choices=[('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)'), ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados')], max_length=2, null=True, verbose_name='Local Diferenciado')),
                ('obito', models.BooleanField(blank=True, default=False, null=True)),
                ('data_obito', models.DateField(blank=True, null=True)),
                ('RG_UF', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='rh.uf_unidade_federativa')),
                ('aluno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.alunos')),
                ('cartorio_uf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatio_cartorio_UF', to='rh.uf_unidade_federativa')),
            ],
        ),
        migrations.CreateModel(
            name='AnoLetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.ano')),
            ],
        ),
        migrations.AddField(
            model_name='alunos',
            name='deficiencia_aluno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.deficiencia_aluno', verbose_name='Informe se o aluno possui deficiência*'),
        ),
        migrations.AddField(
            model_name='alunos',
            name='etnia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.etnia', verbose_name='Etnia do aluno*:'),
        ),
        migrations.AddField(
            model_name='alunos',
            name='nacionalidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.nacionalidade', verbose_name='Nacionalidade*'),
        ),
        migrations.AddField(
            model_name='alunos',
            name='pais_origem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.pais_origem'),
        ),
        migrations.CreateModel(
            name='Profissionais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_especializacao', models.CharField(max_length=100, null=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.cargo')),
                ('nome', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rh.encaminhamentos')),
            ],
        ),
        migrations.CreateModel(
            name='Serie_Escolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('compatibilidade_EducaCenso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.compatibilidade_educacenso')),
                ('nivel_escolar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.grauescolar')),
            ],
        ),
        migrations.CreateModel(
            name='Matriculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_matricula', models.DateField(auto_now=True)),
                ('obervacao', models.TextField(blank=True, max_length=300, null=True)),
                ('escolarizacao_fora', models.CharField(choices=[('3', 'Em domicílio'), ('2', 'Em hospital'), ('1', 'Não recebe')], default=1, max_length=1)),
                ('data_afastamento_inicio', models.DateField(null=True)),
                ('data_afastamento_fim', models.DateField(null=True)),
                ('motivo_afastamento', models.TextField(max_length=200, null=True)),
                ('calcula_media', models.BooleanField(default=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_matricula_alunos', to='gestao_escolar.alunos')),
                ('serie_multiseriada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.serie_escolar')),
            ],
        ),
        migrations.CreateModel(
            name='Trimestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_nome', models.CharField(max_length=14, null=True)),
                ('ano_letivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.anoletivo')),
            ],
        ),
        migrations.CreateModel(
            name='TurmaDisciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria_anual', models.IntegerField(null=True)),
                ('limite_faltas', models.IntegerField(null=True)),
                ('disciplina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.disciplina')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.profissionais')),
            ],
        ),
        migrations.CreateModel(
            name='Trimestral_Notas_Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notas', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('aluno_matriculados', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.matriculas')),
                ('trimestre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.trimestre')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.turmadisciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('turno', models.CharField(choices=[('Verspertino', 'Verspertino'), ('Noturno', 'Noturno'), ('Matutino', 'Matutino')], default=1, max_length=12)),
                ('quantidade_vagas', models.CharField(default=36, max_length=2)),
                ('turma_multiserie', models.BooleanField(default=False, null=True)),
                ('ano_letivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.anoletivo')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.escola')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.serie_escolar')),
            ],
        ),
        migrations.AddField(
            model_name='turmadisciplina',
            name='turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.turmas'),
        ),
        migrations.AddField(
            model_name='matriculas',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.turmas'),
        ),
    ]
