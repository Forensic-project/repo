from django.apps import AppConfig


class TestXssConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_xss'
