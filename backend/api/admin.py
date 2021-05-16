from django.contrib import admin

from backend.api.models import Message


class MessageAdmin(admin.ModelAdmin):
	pass

admin.site.register(Message, MessageAdmin)
