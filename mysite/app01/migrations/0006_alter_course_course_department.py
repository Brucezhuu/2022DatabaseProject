# Generated by Django 4.1.2 on 2022-10-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_department',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
