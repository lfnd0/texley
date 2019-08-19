# Generated by Django 2.2.4 on 2019-08-16 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_auto_20190814_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Professor')),
            ],
            options={
                'verbose_name_plural': 'Turmas',
            },
        ),
    ]