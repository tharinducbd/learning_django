from django.contrib import admin

from .models import House, Student, Subject, Teacher


# class StudentInline(admin.StackedInline):
#     model = Student
#     extra = -3


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


class HouseAdmin(admin.ModelAdmin):
    # Customizations for the object list page
    list_display = ("id", "name", "founder", "emblem", "head", "homeroom",)

    # Customizations for a single object detail page
    fieldsets = [
        (None, {"fields": ["name",]}),
        ("History", {"fields": ["founder", "emblem",]}),
        (None, {"fields": ["homeroom", "head"]}),
    ]
    inlines = [StudentInline]


class StudentAdmin(admin.ModelAdmin):
    # Customizations for the object list page
    list_display = ("name", "house", "id",) # Table header order in list view

    # Customizations for a single object detail page
    fields = ("name", "house", "subjects",) # Field order within object view
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
