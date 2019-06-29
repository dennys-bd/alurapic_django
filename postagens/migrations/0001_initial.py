# Generated by Django 2.2.2 on 2019-06-29 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0004_auto_20190629_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.URLField(max_length=511)),
                ('corpo', models.TextField(max_length=4095)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='post', to='profiles.Profile')),
            ],
        ),
    ]
