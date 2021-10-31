from django.contrib import admin

from .models import Tool, Host, News, ToolInstance


# admin.site.register(Host)
# Define the admin class
class HostAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'house_number', 'street')
    fields = [('first_name', 'last_name'), ('house_number', 'street')]


# Register the admin class with the associated model
admin.site.register(Host, HostAdmin)


# admin.site.register(Tool)
@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('tool', 'host', 'description', 'display_tool_type')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author","news_type", "pub_date", "end_date", "content")
    fields = [( "title", "author", "news_type", "pub_date", "end_date","content")]


# admin.site.register(ToolInstance)
@admin.register(ToolInstance)
class ToolInstanceAdmin(admin.ModelAdmin):

    list_display = ('tool',
                    'status',
                    'borrower',
                    'due_back',
                    'id')
    list_filter = ('status',
                   'due_back')

    fieldsets = (
        (None, {
            'fields': ('id', 'tool', 'purchased')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
