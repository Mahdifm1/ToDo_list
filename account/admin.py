from django.contrib import admin
from django.template.response import TemplateResponse
from collections import OrderedDict

from todoapp.models import Todo
from .models import User


class TodoInline(admin.StackedInline):
    model = Todo
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')
    fields = ('username', 'email', 'date_joined')
    readonly_fields = ('date_joined',)
    inlines = (TodoInline,)
    sortable_by = ('username', 'date_joined')
    list_filter = ('date_joined',)
    search_fields = ('username', 'email')
