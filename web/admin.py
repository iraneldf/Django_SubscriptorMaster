from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from solo.admin import SingletonModelAdmin
from .models import Config, New, Suscriptor, SMS
import os


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

            os.remove(ruta_completa.replace('.tmp', ''))
            os.rename(ruta_completa, ruta_completa.replace('.tmp', ''))

# Register your models here.


@admin.register(Config)
class ConfigAdmin(SingletonModelAdmin):
    pass


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'news']
    list_filter = ['title', 'news']
    actions = [enviar_email]


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
