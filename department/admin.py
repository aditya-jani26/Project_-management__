from django.contrib import admin
from .models import Baseuser, Project

# Register your models here.
admin.site.register(Baseuser)
admin.site.register(Project)