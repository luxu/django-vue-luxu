from django.contrib import admin

from backend.api.models import Message, Sentenciado, Pavilhao


class MessageAdmin(admin.ModelAdmin):
	...


class SentenciadoAdmin(admin.ModelAdmin):
	list_display = [
		'nome',
		'matricula',
		'pavilhao',
	]
	list_filter = [
		'pavilhao',
		'matricula'
	]
	search_fields = [
		'nome',
	]


class PavilhaoAdmin(admin.ModelAdmin):
	list_display = [
		'numero',
		'capacidade',
		'restante'
	]

admin.site.register(Message, MessageAdmin)
admin.site.register(Sentenciado, SentenciadoAdmin)
admin.site.register(Pavilhao, PavilhaoAdmin)
