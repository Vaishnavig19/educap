# Generated by Django 2.1.5 on 2022-06-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('semail', models.CharField(max_length=50)),
                ('smobile', models.IntegerField()),
                ('password', models.CharField(default='12345', max_length=50)),
                ('status', models.CharField(default='active', max_length=10)),
            ],
        ),
    ]