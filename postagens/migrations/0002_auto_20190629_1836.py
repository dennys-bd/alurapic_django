# Generated by Django 2.2.2 on 2019-06-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postagens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_criacao',
            field=models.DateTimeField(),
        ),
    ]
