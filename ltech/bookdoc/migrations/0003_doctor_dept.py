# Generated by Django 4.2.5 on 2023-09-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdoc', '0002_alter_doctor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='dept',
            field=models.TextField(default=''),
        ),
    ]
