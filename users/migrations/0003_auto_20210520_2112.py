# Generated by Django 3.2.1 on 2021-05-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210520_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='datecreated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ph_no',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
    ]