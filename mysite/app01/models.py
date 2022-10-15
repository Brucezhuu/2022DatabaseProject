from django.db import models
from datetime import datetime


# Create your models here.
class StudentInfo(models.Model):
    student_id = models.CharField(max_length=128, unique=True)
    student_password = models.CharField(max_length=128)
    student_email = models.EmailField()
    student_realName = models.CharField(max_length=128)

    # has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.student_realName

    class Meta:
        db_table = 'StudentInfo'
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name


class TeacherInfo(models.Model):
    teacher_id = models.CharField(max_length=128, unique=True)
    teacher_password = models.CharField(max_length=128)
    teacher_email = models.EmailField(unique=True)
    teacher_realName = models.CharField(max_length=128)

    # has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.teacher_realName

    class Meta:
        db_table = 'TeacherInfo'
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name


class Course(models.Model):
    course_id = models.CharField(max_length=128, unique=True)
    course_name = models.CharField(max_length=128, unique=False)
    course_department = models.CharField(max_length=128, unique=False)
    course_teacher_id = models.CharField(max_length=128, unique=False)
    course_teacher_name = models.CharField(max_length=128, unique=False)
    course_info = models.CharField(max_length=1024, unique=False)
    course_pc = models.CharField(max_length=128, unique=False, blank=True)
    course_count = models.IntegerField(unique=False, default=0)
    course_time = models.CharField(max_length=128, unique=False)
    course_total = models.CharField(max_length=128, unique=False)