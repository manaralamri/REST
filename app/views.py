
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Lesson, Student, Teacher, Assignment, Attendance, Grade
from .serializers import LessonSerializer, StudentSerializer, TeacherSerializer, AssignmentSerializer, AttendanceSerializer, GradeSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class LessonViewSet(viewsets.ModelViewSet):


   serializer_class = LessonSerializer
   queryset = Lesson.objects.all()


class StudentViewSet(viewsets.ModelViewSet):


   serializer_class = StudentSerializer
   queryset = Student.objects.all()


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class AssignmentViewSet(viewsets.ModelViewSet):

   serializer_class = AssignmentSerializer
   queryset = Assignment.objects.all()





class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()


class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()



@api_view(['POST'])
def register_user(request):
   if request.method == 'POST':
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







@api_view(['POST'])
def register_user(request):
   if request.method == 'POST':
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def user_login(request):
   if request.method == 'POST':
       username = request.data.get('username')
       password = request.data.get('password')


       user = None
       if '@' in username:
           try:
               user = CustomUser.objects.get(email=username)
           except ObjectDoesNotExist:
               pass


       if not user:
           user = authenticate(username=username, password=password)


       if user:
           token, _ = Token.objects.get_or_create(user=user)
           return Response({'token': token.key}, status=status.HTTP_200_OK)


       return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
   if request.method == 'POST':
       try:
           # Delete the user's token to logout
           request.user.auth_token.delete()
           return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
       except Exception as e:
           return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


