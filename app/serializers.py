from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Lesson, Student, Teacher, Assignment, Attendance, Grade, CustomUser


class LessonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Lesson
       fields = '__all__'#['course_id', 'title', 'content'] يرتيب البيانات كجوسون ملف 


class StudentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Student
       fields = ['name', 'level']# يرتيب البيانات كجوسون ملف 

class TeacherSerializer(serializers.ModelSerializer):
   class Meta:
       model = Teacher
       fields = ['name', 'email', 'classes', 'experience', 'student']# يرتيب البيانات كجوسون ملف 

class AssignmentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Assignment
       fields = '__all__'



class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance 
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade 
        fields = '__all__'







class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = CustomUser
       fields = ['username', 'email', 'password']
       extra_kwargs = {'password': {'write_only': True}}# عندما يتم استعدعاء البيانات الباسورد يكتب فقط وليس يقرا


   def create(self, validated_data):# موقت ينشيء لعمل انشاء مستخدم 
       user = CustomUser(
           username=validated_data['username'],
           email=validated_data['email']
       )
       user.set_password(validated_data['password'])
       user.save()
       return user
