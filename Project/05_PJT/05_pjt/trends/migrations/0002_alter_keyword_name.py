# Generated by Django 4.2.6 on 2023-10-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
