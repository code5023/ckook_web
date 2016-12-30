from django.contrib import admin

from .models import Work, Comment

# Register your models here.
@admin.register(Work, Comment)
class Work(admin.ModelAdmin):
    pass
class Comment(admin.ModelAdmin):
    pass
