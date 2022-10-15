# Generated by Django 4.1.2 on 2022-10-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_studentinfo_teacherinfo_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=128, unique=True)),
                ('course_name', models.CharField(max_length=128)),
                ('course_department', models.CharField(max_length=128)),
                ('course_teacher_id', models.CharField(max_length=128)),
                ('course_teacher_name', models.CharField(max_length=128)),
                ('course_info', models.CharField(max_length=1024)),
                ('course_pc', models.CharField(blank=True, max_length=128)),
                ('course_count', models.IntegerField(default=0)),
                ('course_time', models.CharField(max_length=128)),
                ('course_total', models.CharField(max_length=128)),
            ],
        ),
    ]
