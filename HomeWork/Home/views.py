from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Task, Student, StudentTask
from django.contrib import messages
from datetime import datetime
from django.db.models import Q

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
        if task.end_date.date() >= datetime.now().date():
            studet_i = request.POST['student_id']
            print(studet_i)
            for student in task.studenttask_set.all():
                if int(student.student.student_id) == int(studet_i):
                    messages.error(request, 'already exists')
                    form = StudentForm()
                    context ={
                        'form':form,

                    }
                    return render(request, 'solution.html', context)
            print(form.is_valid())
            if form.is_valid():
                solution = form.save(commit=False)
                try:
                    student_one = Student.objects.get(student_id=studet_i)
                    print(student_one)
                except:
                    solution.save()
                    student_one = Student.objects.get(student_id=studet_i)
                    
                students, created = StudentTask.objects.get_or_create(
                    task=task,
                    student=student_one,
                    student_code = form.cleaned_data.get('student_code'),
                    student_task_file = form.cleaned_data.get('student_task_file')
                    )
                return redirect('task')
                    
        else:
            messages.error(request, 'The time allotted for submitting the assignment has expired.')
    else:
        form = StudentForm()

    context = {
        'form':form,
        'task':task,
    }

    return render(request, 'solution.html', context)