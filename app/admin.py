from django.contrib import admin
from .models import Admin,  Teacher, Lesson, Grade, Assignment, Attendance, Student, CustomUser
# Register your models here.
class AssignmentAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'grade')





  
admin.site.register(Admin)
admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Attendance)
admin.site.register(Student)

admin.site.register(CustomUser)



# Register your models here.
