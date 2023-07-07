from django.apps import AppConfig


class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'

    # add this
    def ready(self):
        from web.jobs import updater
        updater.start()

