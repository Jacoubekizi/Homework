from django.db import models

class Task(models.Model):
    name_item = models.CharField(verbose_name="Type Task", max_length=255)
    title = models. CharField(verbose_name="Title", max_length=255)
    description = models.TextField(verbose_name="Description")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['start_date',]
    
class Student(models.Model):
    student_name = models.CharField(verbose_name="Student_Name", max_length=255)
    student_id = models.IntegerField()
    student_branch_number = models.IntegerField("Student_branch_number")

    def __str__(self):
        return self.student_name
    
class StudentTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_code = models.TextField(verbose_name="Task_code")
    task_file = models.FileField(upload_to="uploads/%Y/%m/%d/")

    def __str__(self):
        return self.student.student_name + " " + self.task.title
    
    def get_name_student_and_name_task(self):
        return self.student.student_name + " " + self.task.title