# Generated by Django 5.1 on 2024-08-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=32, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('nascimento', models.DateField()),
                ('stack', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
