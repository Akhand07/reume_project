# Generated by Django 3.2.3 on 2021-07-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basicdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('father_name', models.CharField(max_length=12)),
                ('mother_name', models.CharField(max_length=12)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=6)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('university_name', models.CharField(max_length=40)),
                ('passing_year', models.IntegerField()),
            ],
        ),
    ]
