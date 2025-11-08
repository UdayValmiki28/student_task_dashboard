from rest_framework import serializers
from .models import Student, Task

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    # 👇 This line adds a readable student name to the Task API
    student_name = serializers.CharField(source='student.name', read_only=True)

    class Meta:
        model = Task
        fields = '__all__'  # includes all model fields + student_name
