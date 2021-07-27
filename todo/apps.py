from django.apps import AppConfig

# Slouzi k pridani appky na stranku (.mysite/settings.py/INSTALLED_APPS)
class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
