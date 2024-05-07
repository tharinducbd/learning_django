from django.contrib import admin

from .models import House, Student, Subject, Teacher

admin.site.register(House)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
