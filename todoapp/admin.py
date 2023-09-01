from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import User, Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'link_to_user', 'added_date', 'done')
    readonly_fields = ('added_date',)
    sortable_by = ('-id', 'title', 'user')
    list_filter = ('added_date',)
    search_fields = ('title', 'user__username')

    def link_to_user(self, obj):
        link = reverse("admin:account_user_change", args=[obj.user_id])
        return format_html('<a href="{}">{}</a>', link, obj.user.username)

    link_to_user.short_description = 'user'
