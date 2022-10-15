from django import forms
from app01 import models

class StuLoginForm(forms.Form):
    student_id = forms.CharField(label="学号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput)


class StuRegisterForm(forms.Form):
    student_id = forms.CharField(label="学号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_password1 = forms.CharField(label="密码", max_length=128,
                                        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    student_password2 = forms.CharField(label="确认密码", max_length=128,
                                        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    student_realName = forms.CharField(label="真实姓名", max_length=128,
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_email = forms.EmailField(label="个人邮箱", widget=forms.EmailInput(attrs={'class': 'form-control'}))


class TeacherLoginForm(forms.Form):
    teacher_id = forms.CharField(label="教工号", max_length=128,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    teacher_password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput)


class TeacherRegisterForm(forms.Form):
    teacher_id = forms.CharField(label="教工号", max_length=128,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    teacher_password1 = forms.CharField(label="密码", max_length=128,
                                        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    teacher_password2 = forms.CharField(label="确认密码", max_length=128,
                                        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    teacher_realName = forms.CharField(label="真实姓名", max_length=128,
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    teacher_email = forms.EmailField(label="个人邮箱", widget=forms.EmailInput(attrs={'class': 'form-control'}))


# 忘记密码表单
class ForgetPwdForm(forms.Form):
    email = forms.EmailField(label='注册邮箱地址', min_length=4,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))


# 个人信息表单
class DetailInfoForm(forms.Form):
    userID = forms.IntegerField(label='用户id')
    # username = forms.CharField(max_length=500, label='用户昵称')
    # realName = forms.CharField(label="真实姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="个人邮箱", widget=forms.EmailInput(attrs={'class': 'form-control'}))


class courseForm(forms.Form):
    course_id = forms.CharField(label='课程id', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_name = forms.CharField(label='课程名称', max_length=128,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_department = forms.CharField(label='开课院系', max_length=128,
                                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_teacher_id = forms.CharField(label='教师工号', max_length=128,
                                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_teacher_name = forms.CharField(label='教师姓名', max_length=128,
                                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_info = forms.CharField(label='课程介绍', max_length=1024,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_pc = forms.CharField(label='前置课程', max_length=128,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_count = forms.IntegerField(label='选课人数')
    course_time = forms.CharField(label='上课时间', max_length=128,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_total = forms.CharField(label='总课时', max_length=128,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Course
        fields = ['title', ]
