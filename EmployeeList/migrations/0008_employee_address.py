# Generated by Django 3.0.6 on 2021-02-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeList', '0007_auto_20210219_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
