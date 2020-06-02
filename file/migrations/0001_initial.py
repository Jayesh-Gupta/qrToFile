# Generated by Django 3.0.5 on 2020-05-19 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100,unique=True)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100,unique=True)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=12)),
            ],
        ),
    ]
