# Generated by Django 4.1.3 on 2023-05-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carmodel_model_carmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
