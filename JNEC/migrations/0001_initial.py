# Generated by Django 5.0 on 2023-12-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Placed_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=50)),
                ('Company_Name', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'Placed_Student',
            },
        ),
    ]