# Generated by Django 3.2.1 on 2021-05-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]