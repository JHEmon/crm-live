from django.apps import AppConfig


class SnippetsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
