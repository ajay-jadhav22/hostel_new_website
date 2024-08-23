# Register your models here.
from django.contrib import admin
from .models import Application

# Register the Student model in the admin interface
admin.site.register(Application)
