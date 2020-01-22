# Generated by Django 2.2.4 on 2020-01-15 23:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('is_estudante', models.BooleanField(default=False)),
                ('is_professor', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.TextField()),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problemas', to='app.Atividade')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('instituto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Professores',
            },
        ),
        migrations.CreateModel(
            name='Submissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.FileField(upload_to='submissoes')),
                ('raw_loc', models.IntegerField()),
                ('raw_lloc', models.IntegerField()),
                ('raw_sloc', models.IntegerField()),
                ('hal_total_h1', models.IntegerField()),
                ('hal_total_h2', models.IntegerField()),
                ('hal_total_N1', models.IntegerField()),
                ('hal_total_N2', models.IntegerField()),
                ('hal_total_vocabulary', models.IntegerField()),
                ('hal_total_length', models.IntegerField()),
                ('hal_total_calculated_length', models.DecimalField(decimal_places=2, max_digits=8)),
                ('hal_total_volume', models.DecimalField(decimal_places=2, max_digits=8)),
                ('hal_total_difficulty', models.DecimalField(decimal_places=2, max_digits=8)),
                ('hal_total_effort', models.DecimalField(decimal_places=2, max_digits=8)),
                ('hal_total_time', models.DecimalField(decimal_places=4, max_digits=8)),
                ('hal_total_bugs', models.DecimalField(decimal_places=4, max_digits=8)),
                ('problema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissoes', to='app.Problema')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Estudante')),
            ],
            options={
                'verbose_name_plural': 'Submissões',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('observacao', models.TextField()),
                ('submissao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Submissao')),
            ],
            options={
                'verbose_name_plural': 'Avaliações',
            },
        ),
        migrations.AddField(
            model_name='atividade',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atividades', to='app.Turma'),
        ),
        migrations.AddField(
            model_name='turma',
            name='estudantes',
            field=models.ManyToManyField(blank=True, to='app.Estudante'),
        ),
        migrations.AddField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turmas', to='app.Professor'),
        ),
    ]