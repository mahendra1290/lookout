# Generated by Django 2.2.2 on 2019-06-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(unique=True)),
                ('name', models.TextField()),
                ('passwd', models.TextField()),
            ],
        ),
    ]