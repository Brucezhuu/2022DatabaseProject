"""
部门 视图函数
"""
import pymysql
from django.shortcuts import render, redirect

from app01.models import StudentInfo, TeacherInfo, Course

from app01.myForm import courseForm

db = pymysql.connect(host='localhost',
                     user='root',
                     password='Zcx20020529',
                     database='mydb',
                     port=3306)
cursor = db.cursor()


def course_add(request):
    """添加部门"""
    title = '添加课程'
    if request.method == 'GET':
        form = courseForm
        return render(request, 'change.html', {"form": form, 'title': title})

    # 用户POST提交数据，数据校验
    form = courseForm(request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        course_id = form.cleaned_data.get("course_id")
        course_name = form.cleaned_data.get("course_name")
        course_department = form.cleaned_data.get("course_department")
        course_teacher_id = form.cleaned_data.get("course_teacher_id")
        course_teacher_name = form.cleaned_data.get("course_teacher_name")
        course_info = form.cleaned_data.get("course_info")
        course_pc = form.cleaned_data.get("course_pc")
        course_count = form.cleaned_data.get("course_count")
        course_time = form.cleaned_data.get("course_time")
        course_total = form.cleaned_data.get("course_total")
        sql = "insert into app01_course(course_id, course_name, course_department, course_teacher_id, course_teacher_name,course_info,course_pc,course_count,course_time,course_total) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            course_id,
            course_name,
            course_department,
            course_teacher_id,
            course_teacher_name,
            course_info,
            course_pc,
            course_count,
            course_time,
            course_total)
        cursor.execute(sql)
        db.commit()
        return redirect('/app01/course/')

    # 校验失败，在页面上显示错误信息
    return render(request, 'change.html', {"form": form, 'title': title})


def course_delete(request, nid):
    sql = "delete from app01_course where course_id = '{}'".format(nid)
    cursor.execute(sql)
    db.commit()
    return redirect('/app01/course/')


def course_edit(request, nid):
    """课程"""
    title = '修改课程信息'
    # 根据id去数据库获取要编辑的那一行数据（对象）
    # row_object = models.Department.objects.filter(id=nid).first()
    sql = "select * from app01_course where course_id='{}'".format(nid)
    cursor.execute(sql)
    info = cursor.fetchone()
    if request.method == 'GET':
        form = courseForm
        return render(request, 'change.html', {"form": form, 'title': title})

    form = courseForm(data=request.POST)
    if form.is_valid():
        # 校验成功
        course_id = form.cleaned_data.get("course_id")
        course_name = form.cleaned_data.get("course_name")
        course_department = form.cleaned_data.get("course_department")
        course_teacher_id = form.cleaned_data.get("course_teacher_id")
        course_teacher_name = form.cleaned_data.get("course_teacher_name")
        course_info = form.cleaned_data.get("course_info")
        course_pc = form.cleaned_data.get("course_pc")
        course_count = form.cleaned_data.get("course_count")
        course_time = form.cleaned_data.get("course_time")
        course_total = form.cleaned_data.get("course_total")
        sql = "update app01_course set course_id='{}',course_name='{}',course_department='{}',course_teacher_id='{}',course_teacher_name='{}',course_info='{}',course_pc='{}',course_count='{}',course_time='{}',course_total='{}' where course_id='{}'".format(
            course_id, course_name, course_department, course_teacher_id, course_teacher_name, course_info, course_pc,
            course_count, course_time, course_total, nid)
        cursor.execute(sql)
        db.commit()
        return redirect('/app01/course/')

    # 校验失败，提示错误信息
    return render(request, 'change.html', {"form": form, 'title': title})


def showCourse(request):
    sql = "select * from app01_course"
    cursor.execute(sql)
    alls = list(cursor.fetchall())
    return render(request, "course_list.html", {"queryset": alls})
