from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Task, Student, StudentTask
from django.contrib import messages
from datetime import datetime
from django.db.models import Q
from django.utils import timezone
# Create your views here.


def TaskFormView(request):
    tasks = Task.objects.all()

    context = {
        'tasks':tasks
    }

    return render(request, 'tasks.html', context)

def StudentFormView(request, task_id):

    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)     
        if timezone.now() < task.end_date:
            student_i = request.POST['student_id']
            for student in task.studenttask_set.all():
                if int(student.student.student_id) == int(student_i):
                    messages.error(request, 'already exists')
                    form = StudentForm()
                    context ={
                        'form':form,

                    }
                    return render(request, 'solution.html', context)
                
            if form.is_valid():
                solution = form.save(commit=False)
                st_id = form.cleaned_data['student_id']
                student_branch_number = form.cleaned_data['student_branch_number']
                if int(st_id) <= 0 or int(student_branch_number) <= 0:
                    messages.error(request, "please enter positave number.")
                else:
                    student_one, created = Student.objects.get_or_create(student_name=form.cleaned_data['student_name'],student_id=st_id, student_branch_number=student_branch_number)
                    if str(form.cleaned_data['task_file']).endswith('.doc') or str(form.cleaned_data['task_file']).endswith('.docx'):
                        students, created = StudentTask.objects.get_or_create(
                            task=task,
                            student=student_one,
                            student_code = form.cleaned_data['student_code'],
                            task_file = form.cleaned_data['task_file']
                            )
                        return redirect('task')
                    else:
                        messages.error(request, 'only accept doc or docx')
                    
        else:
            messages.error(request, 'The time allotted for submitting the assignment has expired.')
    else:
        form = StudentForm()

    context = {
        'form':form,
        'task':task,
    }

    return render(request, 'solution.html', context)
