# Generated by Django 4.2.1 on 2023-05-29 11:48

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
                ('name', models.CharField(max_length=100)),
                ('reg_no', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]
