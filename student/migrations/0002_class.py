# Generated by Django 2.2.24 on 2021-09-13 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]