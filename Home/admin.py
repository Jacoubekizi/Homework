from django.contrib import admin
from .models import Task, Student, StudentTask
from django.contrib.admin import ModelAdmin

# Register your models here.

class TaskAdmin(ModelAdmin):
    list_display = ['name_item', 'title', 'description', 'start_date', 'end_date']

    fieldsets = (
        ('Add_Name_Item', {
            'fields':['name_item',]
        }),
        ('Add_Information_Task', {
            'fields':['title', 'description', 'start_date', 'end_date']
        }),
    )


class StudentAdmin(ModelAdmin):
    list_display = ['student_id', 'student_name',]
    list_per_page = 10

    search_fields = ['student_id', 'student_name', 'student_branch_number']


class StudentTaskAdmin(ModelAdmin):
    list_display = ['get_name_student_and_name_task','student_code', 'task_file']

    list_per_page = 50

    
admin.site.register(Task, TaskAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentTask, StudentTaskAdmin)