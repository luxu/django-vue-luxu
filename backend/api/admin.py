from django.contrib import admin

from backend.api.models import Message


class MessageAdmin(admin.ModelAdmin):
	...

admin.site.register(Message, MessageAdmin)
