from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'  # To'g'ri app nomi

    def ready(self):
        # To'g'ri import yo'lidan foydalaning
        from apps.users import signals  # "users" o'rniga "apps.users"