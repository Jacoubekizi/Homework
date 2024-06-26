# Generated by Django 5.0 on 2024-05-17 15:29

import django.db.models.deletion
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
                ('student_name', models.CharField(max_length=255, verbose_name='Student_Name')),
                ('student_id', models.IntegerField()),
                ('student_branch_number', models.IntegerField(verbose_name='Student_branch_number')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_item', models.CharField(max_length=255, verbose_name='Item_Name')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='StudentTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_code', models.TextField(verbose_name='Task_code')),
                ('task_file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.student')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.task')),
            ],
        ),
    ]
