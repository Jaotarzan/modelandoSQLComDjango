# Generated by Django 4.2.6 on 2023-10-18 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_titulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAtuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]
