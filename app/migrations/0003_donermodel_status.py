# Generated by Django 4.1.2 on 2022-10-19 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_bloodgroupchoices_donermodel_bloodgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='donermodel',
            name='Status',
            field=models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], default='unmarried', max_length=25),
        ),
    ]