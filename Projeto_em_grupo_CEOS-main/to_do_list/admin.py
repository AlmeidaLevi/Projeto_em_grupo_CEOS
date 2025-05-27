from django.contrib import admin
from to_do_list import models

# Register your models here.
@admin.register(models.Task)
class TaskAdmim(admin.ModelAdmin):
    list_display = 'id', 'title',
