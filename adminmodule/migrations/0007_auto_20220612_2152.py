# Generated by Django 2.1.5 on 2022-06-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0006_auto_20220612_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='name',
            field=models.CharField(default='abc', max_length=50),
        ),
        migrations.AddField(
            model_name='notes',
            name='name',
            field=models.CharField(default='abc', max_length=50),
        ),
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default='abc', max_length=50),
        ),
    ]
