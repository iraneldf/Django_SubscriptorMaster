from django.contrib import admin
from .models import Config, New, Suscriptor

# Register your models here.
@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    pass

@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
    pass

