# Generated by Django 4.2.5 on 2023-09-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdoc', '0013_alter_makeappointment_iswaiting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeappointment',
            name='iswaiting',
            field=models.BooleanField(default=False),
        ),
    ]
