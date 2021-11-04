from django.contrib import admin
from .models import Contact, Teacher, Branch

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'phone_number', 'email', 'message', 'created_date'
    )

    list_filter = ('name',)
    search_field = ('name__startswith',)


admin.site.register(Contact, ContactAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email_teacher",
        "phone_teacher",
        "speciality",
        "created_date",
    )
    list_filter = ("first_name",)
    search_fields = ("first_name__startswith",)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Branch)
