# Generated by Django 4.1.2 on 2022-10-19 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('bloodgroupchoices', models.CharField(choices=[('o+ve', 'o+ve'), ('A-ve', 'A-ve')], max_length=5)),
                ('Age', models.IntegerField()),
                ('contact', models.CharField(max_length=15)),
                ('Altcontact', models.CharField(blank=True, max_length=15, null=True)),
                ('Address', models.CharField(max_length=200)),
                ('premedhis', models.CharField(max_length=300)),
            ],
        ),
    ]