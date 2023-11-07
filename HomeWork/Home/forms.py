from django import forms
from .models import Task, Student

class StudentForm(forms.ModelForm):

    student_code = forms.CharField(
                            widget=forms.Textarea(attrs={
                            'rows': 5,
                            })
                        ,)
    student_task_file = forms.FileField()

    class Meta:
        model = Student
        fields = ['student_name', 'student_id', 'student_branch_number', 'student_code', 'student_task_file']



class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['id', ]