from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from solo.admin import SingletonModelAdmin
from .models import Config, New, Suscriptor, SMS


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

# Register your models here.


@admin.register(Config)
class ConfigAdmin(SingletonModelAdmin):
    pass


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['title']
    actions = [enviar_email]


@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
    pass


@admin.register(SMS)
class SMSAdmin(admin.ModelAdmin):
    list_display = ['sms', 'longitud']
    pass
