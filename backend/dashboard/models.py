from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, default='Pending')  # Pending / Completed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.student.name}"
