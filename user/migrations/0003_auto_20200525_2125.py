# Generated by Django 3.0.5 on 2020-05-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200525_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='dep_sequence',
            field=models.CharField(max_length=100),
        ),
    ]
