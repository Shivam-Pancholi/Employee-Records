# Generated by Django 3.0.6 on 2021-02-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeList', '0004_auto_20210218_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
