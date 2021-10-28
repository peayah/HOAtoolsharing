from django.contrib import admin

from .models import Tool, Host, ToolType, ToolInstance

admin.site.register(Tool)
admin.site.register(Host)
admin.site.register(ToolType)
admin.site.register(ToolInstance)