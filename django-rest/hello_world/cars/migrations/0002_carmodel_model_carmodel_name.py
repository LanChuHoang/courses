# Generated by Django 4.1.3 on 2023-05-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='model',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]