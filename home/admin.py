from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'phone_number', 'email', 'message', 'created_date'
    )

    list_filter = ('name',)
    search_field = ('name__startswith',)


admin.site.register(Contact, ContactAdmin)
