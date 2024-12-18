# Generated by Django 5.1.3 on 2024-11-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('yop', models.IntegerField(max_length=4)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
    ]
