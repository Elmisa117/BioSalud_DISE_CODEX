from django.apps import AppConfig

class TareasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tareas'

    def ready(self):
        from . import admin_dispositivotoken