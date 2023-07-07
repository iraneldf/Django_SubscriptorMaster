import os

from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail


@admin.action(description='Enviar noticia a usuarios subscritos')
def enviar_email(modeladmin, request, queryset):
    recipient_list = [
        suscriptor.email for suscriptor in Suscriptor.objects.all()]
    config = Config.objects.first()
    for new in queryset:
        # Enviar email
        subject = new.title
        message = f'Desde {config.business_name}:\n{new.news}'
        email_from = settings.EMAIL_HOST_USER

        send_mail(subject, '', email_from,
                  recipient_list=recipient_list, html_message=message)


import json

from django.contrib import admin, messages
from solo.admin import SingletonModelAdmin

from .models import Config, New, Suscriptor, SMS


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
    print(datos)
    with open('news.json', 'w') as archivo:
        for diccionario in datos:
            json.dump(diccionario, archivo)
            archivo.write('\n')

    # Imprimir el objeto JSON codificado

    messages.info(request, 'Tarea ejecutandose en segundo plano')


@admin.action(description='Enviar noticia a usuarios subscritos')
def enviar_sms(modeladmin, request, queryset):
    numbers = Suscriptor.objects.exclude(phone__isnull=True)
    sms_dir = settings.SMS_DIR
    print(numbers)
    print(sms_dir)
    print(queryset)

    for number in numbers:
        for sms in queryset:
            nombre_archivo = f'{number.phone}__{sms.pk}.txt.tmp'
            ruta_completa = os.path.join(sms_dir, nombre_archivo)

            archivo = open(ruta_completa, "w")

            # para que respete la cantidad de espacios en blanco
            [archivo.write(linea) for linea in sms.sms.split('\n')]

            archivo.close()

            os.rename(ruta_completa, ruta_completa.replace('.tmp', ''))

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


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'news']
    list_filter = ['title', 'news']

    actions = [enviar_email_wrapper]


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
