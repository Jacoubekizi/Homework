from django import forms
from .models import Task, Student
from django.utils.translation import gettext_lazy as _




class StudentForm(forms.ModelForm):

    student_code = forms.CharField(label="Code", widget=forms.Textarea(attrs={
        'rows': 5,
        'placeholder':'أدخل الكود'
    }),)
    student_name = forms.CharField(label="Student name", widget=forms.TextInput(attrs={
        'placeholder':'أدخل الاسم الثلاثي'
    }))
    student_id = forms.IntegerField(label="Studetn id", widget=forms.NumberInput(attrs={
        'placeholder':'أدخل الرقم الجامعي'
    }))

    student_branch_number = forms.IntegerField(label='Student branch number', widget=forms.NumberInput(attrs={
        'placeholder':'أدخل رقم الفئة'
    }
    ))
    task_file = forms.FileField(label="Task File", widget=forms.FileInput(attrs={
        'placeholder': 'يحتوي شرح الكود word قم بإدخال ملف',
 
    }))


    class Meta:
        model = Student
        fields = ['student_name', 'student_id', 'student_branch_number', 'student_code', 'task_file']


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['id', ]