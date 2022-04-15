from django.contrib import admin

# Register your models here.
from .models import Student, Cursus


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone') # Define Student View

class CursusAdmin(admin.ModelAdmin):
    list_display = ('scholar_year', 'name', 'year_from_bac') # Define Cursor View


admin.site.register(Student, StudentAdmin)
admin.site.register(Cursus, CursusAdmin)
