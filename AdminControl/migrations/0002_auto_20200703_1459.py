# Generated by Django 3.0 on 2020-07-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminControl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='username',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
