# Generated by Django 4.0.6 on 2022-08-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_alter_hostelite_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelite',
            name='sic',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
