from django.contrib import admin
from .models import ToDo


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_complete', 'user')
    list_filter = ('is_complete', 'user')
    search_fields = ('title', 'user__username')


admin.site.register(ToDo, TaskAdmin)
