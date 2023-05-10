from django.contrib import admin
from logic import models

# Register your models here.
admin.site.register(models.Building)
admin.site.register(models.Campus)
admin.site.register(models.Classroom)
admin.site.register(models.Course)
