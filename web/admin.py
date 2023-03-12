from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Config, New, Suscriptor

# Register your models here.
@admin.register(Config)
class ConfigAdmin(SingletonModelAdmin):
    pass

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    pass

@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
    pass