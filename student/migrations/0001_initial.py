# Generated by Django 4.1.3 on 2022-11-18 08:37

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
                ('name', models.TextField(default='None')),
                ('email', models.TextField(default='None')),
                ('password', models.TextField(default='None')),
                ('subject', models.TextField(default='None')),
                ('mob', models.BigIntegerField(default=0)),
            ],
        ),
    ]
