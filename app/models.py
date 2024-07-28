from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
class Lesson(models.Model):    
    course_id = models.IntegerField(primary_key = True) 
    title = models.CharField(max_length=100)    
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):        
        return self.title



class Student(models.Model):

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    classes = models.ManyToManyField(Lesson, related_name='students')

    def str(self):
        return self.user.username
    
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    classes = models.CharField(max_length=200)

    def str(self):
        return self.user.name

    
class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)





class Attendance(models.Model):    
    PRESENT = 'P'
    ABSENT = 'A'   
    STATUS_CHOICES = [
        (PRESENT, 'Present'),        
        (ABSENT, 'Absent'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')    
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()   
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=ABSENT)
    def __str__(self):
        return f"{self.student.name} - {self.lesson.title} on {self.date}: {self.get_status_display()}"


class Assignment(models.Model):
   assignment_id = models.IntegerField(primary_key = True)
   title = models.CharField(max_length=100)
   description = models.CharField(max_length=250)
   due_date = models.DateTimeField(auto_now_add=True)
   grade = models.CharField(max_length=100)
   lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
   student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

   def str(self):
       return self.title
   
class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def str(self):
        return f'{self.student.user.username} - {self.grade}'







class CustomUser(AbstractUser):
   email = models.EmailField(unique=True)


   # Add custom fields here, if needed


   def __str__(self):
       return self.username
