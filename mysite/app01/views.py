import re

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app01.myForm import StuLoginForm,StuRegisterForm,TeacherRegisterForm,TeacherLoginForm
from app01.models import StudentInfo, TeacherInfo


# Create your views here.
def index(request):
    return HttpResponse("Welcome")


def user_list(request):
    return render(request, "user_list.html")


@csrf_exempt
def StudentRegister(request):
    if request.method == 'POST':
        register_form = StuRegisterForm(request.POST)
        if register_form.is_valid():
            stu_id = register_form.cleaned_data.get('student_id')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            realName = register_form.cleaned_data.get('realName')

            # 检测两次密码是否一致
            if password1 != password2:
                return JsonResponse({'error': 4004, 'msg': '两次输入的密码不一致'})
            # 检测密码不符合规范：8-18，英文字母+数字
            if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password1):
                return JsonResponse({'error': 4003, 'msg': '密码不符合规范'})

            # 成功
            new_student = StudentInfo()
            new_student.student_realName = realName
            new_student.student_password = password1
            new_student.student_email = email
            new_student.save()
            return JsonResponse({'error': 0, 'msg': '学生注册成功!'})
    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
def StudentLogin(request):
    if request.method == 'POST':
        login_form = StuLoginForm(request.POST)

        if login_form.is_valid():
            student_id = login_form.cleaned_data.get('student_id')
            student_password = login_form.cleaned_data.get('student_password')
            try:
                user = StudentInfo.object.get(student_id=student_id)
            except:
                return JsonResponse({'error': 4002, 'msg': '学号不存在'})
            return JsonResponse({
                'error': 0,
                'msg': "登录成功",
                'student_name': user.student_realName,
                'student_id': user.student_id,
                'email': user.useremail,
            })
    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
def TeacherRegister(request):
    if request.method == 'POST':
        register_form = TeacherRegisterForm(request.POST)
        if register_form.is_valid():
            teacher_id = register_form.cleaned_data.get('teacher_id')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            realName = register_form.cleaned_data.get('realName')

            # 检测两次密码是否一致
            if password1 != password2:
                return JsonResponse({'error': 4004, 'msg': '两次输入的密码不一致'})
            # 检测密码不符合规范：8-18，英文字母+数字
            if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password1):
                return JsonResponse({'error': 4003, 'msg': '密码不符合规范'})

            # 成功
            new_teacher = TeacherInfo()
            new_teacher.teacher_id = teacher_id
            new_teacher.teacher_password = password2
            new_teacher.teacher_realName = realName
            new_teacher.teacher_email = email
            new_teacher.save()
            return JsonResponse({'error': 0, 'msg': '老师注册成功!'})
    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
def TeacherLogin(request):
    if request.method == 'POST':
        login_form = TeacherLoginForm(request.POST)

        if login_form.is_valid():
            teacher_id = login_form.cleaned_data.get('teacher_id')
            teacher_password = login_form.cleaned_data.get('teacher_password')
            try:
                user = TeacherInfo.object.get(teacher_id=teacher_id)
            except:
                return JsonResponse({'error': 4002, 'msg': '教工号不存在'})
            return JsonResponse({
                'error': 0,
                'msg': "登录成功",
                'student_id': user.teacher_id,
                'email': user.useremail,
                'realName': user.realName,
            })
    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})
