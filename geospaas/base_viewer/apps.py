from django.apps import AppConfig


class BaseViewerConfig(AppConfig):
    name = 'geospaas.base_viewer'
    default_auto_field = "django.db.models.AutoField"
