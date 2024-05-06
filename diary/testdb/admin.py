from django.contrib import admin

from .models import House, Student, Subject, Teacher


class HouseAdmin(admin.ModelAdmin):
    list_display = ("name", "founder", "emblem", "head", "id")

class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "house", "pk", "id")
    filter_horizontal = ("subjects",)

class TeacherAdmin(admin.ModelAdmin):
    filter_horizontal = ("subjects",)


admin.site.register(House, HouseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject)
admin.site.register(Teacher, TeacherAdmin)
