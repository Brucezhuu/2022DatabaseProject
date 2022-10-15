import re

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from app01.myForm import StuLoginForm, StuRegisterForm, TeacherRegisterForm, TeacherLoginForm, courseForm
from app01.models import StudentInfo, TeacherInfo

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='Zcx20020529',
                     database='mydb',
                     port=3306)
cursor = db.cursor()


@csrf_exempt
def logout(request):
    """注销"""
    request.session.clear()
    return redirect('/app01/toLogin/')


@csrf_exempt
def login(request):
    return render(request, 'login.html')


@csrf_exempt
def register(request):
    return render(request, 'register.html')


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
            password1 = register_form.cleaned_data.get('student_password1')
            password2 = register_form.cleaned_data.get('student_password2')
            email = register_form.cleaned_data.get('student_email')
            realName = register_form.cleaned_data.get('student_realName')
            findStuNo = "select * from studentinfo where student_id='{}'".format(stu_id)
            findEmail = "select * from studentinfo where student_email='{}'".format(email)
            cursor.execute(findStuNo)
            student = cursor.fetchall()
            if len(student) == 1:
                messages.info(request, 'student_id has been registered!')
                # return JsonResponse({'error': 4006, 'msg': 'student_id has been registered!'})
                return redirect("/app01/toRegister/")
            cursor.execute(findEmail)
            email = cursor.fetchall()
            if len(email) == 1:
                messages.info(request, 'current email has been registered!')
                # return JsonResponse({'error': 4007, 'msg': 'current email has been registered!'})
                return redirect("/app01/toRegister/")
            # 检测两次密码是否一致
            if password1 != password2:
                messages.info(request, "please make sure the second password you input is same as first one")
                # return JsonResponse({'error': 4004, 'msg': 'please make sure the second password you input is same as first one'})
                return redirect("/app01/toRegister/")
            # 检测密码不符合规范：8-18，英文字母+数字
            if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password1):
                messages.info(request, "密码不符合规范")
                # return JsonResponse({'error': 4003, 'msg': '密码不符合规范'})
                return redirect("/app01/toRegister/")

            sql = "insert into studentinfo(student_id,student_password,student_email,student_realName) values ('{}','{}','{}','{}')".format(
                stu_id, password1, email, realName)
            cursor.execute(sql)
            db.commit()
            return redirect("login")
        return JsonResponse({'error': 8899, 'msg': 'Invalid RegisterForm'})
    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
def StudentLogin(request):
    if request.method == 'POST':
        login_form = StuLoginForm(request.POST)

        if login_form.is_valid():
            student_id = login_form.cleaned_data.get('student_id')
            student_password = login_form.cleaned_data.get('student_password')
            sql = "select * from studentinfo where student_id='{}'".format(student_id)
            cursor.execute(sql)
            student = cursor.fetchall()
            if len(student) == 0:
                messages.info(request, 'Username OR password is incorrect')
                return redirect('/app01/toLogin/')
            else:
                sql2 = "select * from studentinfo where student_password='{}'".format(student_password)
                cursor.execute(sql2)
                row = cursor.fetchone()
                print(row)
                if row is not None:
                    # return JsonResponse({
                    #     'error': 0,
                    #     'msg': "登录成功",
                    #     'student_realName': row[4],
                    #     'student_id': student_id,
                    #     'email': row[3],
                    # })
                    return redirect("course")
                else:
                    messages.info(request, 'Username OR password is incorrect')
                    return redirect('/app01/toLogin/')
        return JsonResponse({'error': 8899, 'msg': 'Invalid LoginForm!'})

    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
def update_pwd_student(request):
    if request.method == 'POST':
        register_email = request.POST.get("student_email")
        password = request.POST.get("password")
        findEmail = "select * from studentinfo where student_email = '{}'".format(register_email)
        cursor.execute(findEmail)
        info = cursor.fetchall()
        if len(info) == 0:
            return JsonResponse({'error': 4002, 'msg': '邮箱号不存在'})

        if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password):
            return JsonResponse({'error': 4001, 'msg': '密码不符合规范'})

        update = "Update studentinfo set student_password = '{}' where student_email = '{}'".format(password,
                                                                                                    register_email)
        cursor.execute(update)
        db.commit()
        # del request.session["code"]  # 删除session
        return JsonResponse({'error': 0, 'msg': "密码已重置"})

    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})
