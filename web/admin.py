import json

from django.contrib import admin, messages
from solo.admin import SingletonModelAdmin

from .models import Config, New, Suscriptor, SMS, EmailImg


# Django-sheduler
@admin.action(description='Enviar noticia a usuarios subscritos')
def enviar_email_wrapper(modeladmin, request, queryset):
    # Crear un diccionario de Python que represente los datos que deseas codificar en formato JSON
    datos = []
    for q in queryset:
        datos.append({
            'titulo': q.title,
            'noticia': q.news,
        })
    with open('news.json', 'w') as archivo:
        for diccionario in datos:
            json.dump(diccionario, archivo)
            archivo.write('\n')

    # Imprimir el objeto JSON codificado

    messages.info(request, 'Tarea ejecutandose en segundo plano')


@admin.action(description='Enviar noticia a usuarios subscritos')
def enviar_sms(modeladmin, request, queryset):
    datos = []
    for q in queryset:
        datos.append({
            'pk': q.pk,
            'sms': q.sms,
        })
    with open('sms.json', 'w') as archivo:
        for diccionario in datos:
            json.dump(diccionario, archivo)
            archivo.write('\n')

    messages.info(request, 'Tarea ejecutandose en segundo plano')


# Register your models here.


@admin.register(Config)
class ConfigAdmin(SingletonModelAdmin):
    pass


class ImgInLine(admin.StackedInline):
    model = EmailImg


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'news']
    list_filter = ['title', 'news']
    actions = [enviar_email_wrapper]
    inlines = [ImgInLine]


@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
    search_fields = ['email', 'phone']
    list_filter = ['email', 'phone']


@admin.register(SMS)
class SMSAdmin(admin.ModelAdmin):
    list_display = ['sms', 'longitud']
    search_fields = ['sms']
    list_filter = ['sms']
    actions = [enviar_sms]
