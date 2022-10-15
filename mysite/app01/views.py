import re

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app01.myForm import StuLoginForm, StuRegisterForm, TeacherRegisterForm, TeacherLoginForm, courseForm
from app01.models import StudentInfo, TeacherInfo

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='Zcx20020529',
                     database='mydb')
cursor = db.cursor()


@csrf_exempt
def course_add(request):
    """添加课程"""

    # 用户POST提交数据，数据校验
    # 如果数据合法，保存到数据库
    course_id = request.POST.get("course_id")
    course_name = request.POST.get("course_name")
    course_teacher_name = request.POST.get("course_teacher_name")
    course_info = request.POST.get("course_info")
    course_time = request.POST.get("course_time")

    # course_total = form.cleaned_data.get("course_total")
    sql = "insert into app01_course(" \
          "course_id, course_name, course_teacher_name,course_info, " \
          "course_time,course_department,course_teacher_id,course_count,course_total,course_pc)" \
          " values ('{}','{}','{}','{}','{}','','',0,'','')".format(
        course_id,
        course_name,
        course_teacher_name,
        course_info,
        course_time)
    cursor.execute(sql)
    db.commit()
    return JsonResponse({"error": 0})


@csrf_exempt
def course_delete(request):
    course_id = request.POST.get("course_id")
    sql = "delete from app01_course where course_id = '{}'".format(course_id)
    cursor.execute(sql)
    db.commit()
    return JsonResponse({'error': 0})


@csrf_exempt
def course_edit(request):
    """课程"""
    title = '修改课程信息'
    # 根据id去数据库获取要编辑的那一行数据（对象）
    course_id = request.POST.get("course_id")
    sql = "select * from app01_course where course_id='{}'".format(course_id)
    cursor.execute(sql)

    # 校验成功
    course_name = request.POST.get("course_name")
    course_teacher_name = request.POST.get("course_teacher_name")
    course_info = request.POST.get("course_info")
    course_time = request.POST.get("course_time")
    sql = "update app01_course set course_id='{}',course_name='{}',course_teacher_name='{}',course_info='{}',course_time='{}' where course_id='{}'".format(
        course_id, course_name, course_teacher_name, course_info, course_time, course_id)
    cursor.execute(sql)
    db.commit()

    # 校验失败，提示错误信息
    return JsonResponse({"error": 0})


@csrf_exempt
def showCourse(request):
    sql = "select * from app01_course"
    cursor.execute(sql)
    alls = cursor.fetchall()
    res = []
    info = ["id", "course_id", "course_name", "course_department", "course_teacher_id", "course_teacher_name",
            "course_info", "course_pc", "course_count", "course_time", "course_total"]
    for el in alls:
        dic = dict(zip(info, el))
        res.append(dic)

    # return res
    return JsonResponse({'data': res})


@csrf_exempt
def toLogin(request):
    return render(request, 'login.html')


@csrf_exempt
def toRegister(request):
    return render(request, 'toRegister.html')


@csrf_exempt
def register(request):
    student_id = request.POST.get("student_id")
    passwd = request.POST.get("passwd")
    email = request.POST.get('email')
    realName = request.POST.get("realName")
    if student_id and passwd:
        cursor.execute(
            "insert into studentinfo(student_id,student_password, student_email, student_realName) values (\'{}\',\'{}\',\'{}\',\'{}\')".format(
                student_id, passwd, email, realName))
        return HttpResponse("注册成功,欢迎{}!".format(realName))
    else:
        return HttpResponse("学号和密码不得为空，请重新输入!")


@csrf_exempt
def login(request):
    student_id = request.POST.get("student_id")
    passwd = request.POST.get("passwd")
    if student_id and passwd:
        cursor.execute(
            "select student_id from studentinfo where student_id=\'{}\' and student_password=\'{}\'".format(student_id,
                                                                                                            passwd))
        if cursor.fetchone() is None:
            return HttpResponse("账号密码错误，请输入正确的账号密码！")
        else:
            return HttpResponse("登陆成功!欢迎！")
    else:
        return HttpResponse("请输入正确的账号密码！")


@csrf_exempt
# Create your views here.
def index(request):
    return HttpResponse("Welcome")


@csrf_exempt
def user_list(request):
    return render(request, "user_list.html")


@csrf_exempt
def StudentRegister(request):
    if request.method == 'POST':

        stu_id = request.POST.get('student_id')
        password1 = request.POST.get('student_password1')
        password2 = request.POST.get('student_password2')
        email = request.POST.get('student_email')
        realName = request.POST.get('student_realName')

        findStuNo = "select * from studentinfo where student_id='{}'".format(stu_id)
        findEmail = "select * from studentinfo where student_email='{}'".format(email)
        cursor.execute(findStuNo)
        student = cursor.fetchall()
        if len(student) == 1:
            return JsonResponse({'error': 4006, 'msg': '当前学号已经存在，不能重复注册'})
        cursor.execute(findEmail)
        emails = cursor.fetchall()
        if len(emails) == 1:
            return JsonResponse({'error': 4007, 'msg': '当前邮箱已经存在，不能重复注册'})

        # 检测两次密码是否一致
        if password1 != password2:
            return JsonResponse({'error': 4004, 'msg': '两次输入的密码不一致'})
        sql = "insert into studentinfo(student_id,student_password,student_email,student_realName) values ('{}','{}','{}','{}')".format(
            stu_id, password1, email, realName)
        cursor.execute(sql)
        db.commit()
        return JsonResponse({'error': 0, 'msg': '学生注册成功!'})

    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
def StudentLogin(request):
    if request.method == 'POST':
        login_form = StuLoginForm(request.POST)

        if login_form.is_valid():
            student_id = login_form.cleaned_data.get('student_id')
            student_password = login_form.cleaned_data.get('student_password')
            sql = "select * from studentinfo where student_id='{}'".format(student_id)
            cnt = cursor.execute(sql)

            if cnt == 0:
                return JsonResponse({'code': 4002, 'msg': '学号不存在'})
            else:
                row = cursor.fetchone()
                if row[1] != student_password:
                    return JsonResponse({
                        'code': 4004,
                        'msg': "密码错误",
                    })
                else:
                    return JsonResponse({
                        'code': 0,
                        'msg': "登录成功",
                        'student_realName': row[3],
                        'email': row[2],
                    })

        return JsonResponse({'code': 8899, 'msg': '格式不对'})

    return JsonResponse({'code': 2001, 'msg': '请求方式错误'})


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
            # new_teacher = TeacherInfo()
            # new_teacher.teacher_id = teacher_id
            # new_teacher.teacher_password = password2
            # new_teacher.teacher_realName = realName
            # new_teacher.teacher_email = email
            # new_teacher.save()
            sql = 'insert into studentinfo(teacher_id,teacher_password,teacher_email,teacher_realName) values ("teacher_id","password1","email","realName")'
            cursor.execute(sql)
            db.commit()
            return JsonResponse({'error': 0, 'msg': '老师注册成功!'})
    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
def TeacherLogin(request):
    if request.method == 'POST':
        login_form = TeacherLoginForm(request.POST)

        if login_form.is_valid():
            teacher_id = login_form.cleaned_data.get('teacher_id')
            teacher_password = login_form.cleaned_data.get('teacher_password')
            # try:
            #     user = TeacherInfo.object.get(teacher_id=teacher_id)
            # except:
            #     return JsonResponse({'error': 4002, 'msg': '教工号不存在'})
            sql = "select * from teacherinfo where teacher_id='{}'".format(teacher_id)
            cnt = cursor.execute(sql)
            if cnt == 0:
                return JsonResponse({'error': 4002, 'msg': '教工号不存在'})
            else:
                row = cursor.fetchone()
                return JsonResponse({
                    'error': 0,
                    'msg': "登录成功",
                    'student_id': teacher_id,
                    'email': row[3],
                    'realName': row[4],
                })
    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
def update_pwd_student(request):
    if request.method == 'POST':
        register_email = request.POST.get("student_email")
        password = request.POST.get("password")
        try:
            user = StudentInfo.objects.get(student_email=register_email)
        except:
            return JsonResponse({'error': 4003, 'msg': '邮箱不存在'})
        if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password):
            return JsonResponse({'error': 4001, 'msg': '密码不符合规范'})
        user.userpassword = password
        user.save()
        del request.session["code"]  # 删除session
        msg = "密码已重置"
        return JsonResponse({'error': 0, 'msg': msg})

    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
def update_pwd_teacher(request):
    if request.method == 'POST':
        register_email = request.POST.get("teacher_email")
        password = request.POST.get("password")
        try:
            user = TeacherInfo.objects.get(teacher_email=register_email)
        except:
            return JsonResponse({'error': 4003, 'msg': '邮箱不存在'})
        if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password):
            return JsonResponse({'error': 4001, 'msg': '密码不符合规范'})
        user.userpassword = password
        user.save()
        del request.session["code"]  # 删除session
        msg = "密码已重置"
        return JsonResponse({'error': 0, 'msg': msg})

    return JsonResponse({'error': 2001, 'msg': '请求方式错误'})
