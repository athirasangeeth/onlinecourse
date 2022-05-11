# Generated by Django 4.0.2 on 2022-05-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=10)),
                ('password', models.TextField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'registration',
            },
        ),
    ]
