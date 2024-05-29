from django.contrib import admin

from .models import House, Student, Subject, Teacher


class HouseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "founder", "emblem", "head", "homeroom",)
    fieldsets = [
        (None, {"fields": ["name",]}),
        ("History", {"fields": ["founder", "emblem",]}),
        (None, {"fields": ["homeroom", "head"]}),
    ]


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "house", "id",) # To control the order of fields in list view
    fields = ("name", "house", "subjects",) # To control the field order within an object view
    filter_horizontal = ("subjects",)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "id",)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "id")
    filter_horizontal = ("subjects",)


admin.site.register(House, HouseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
