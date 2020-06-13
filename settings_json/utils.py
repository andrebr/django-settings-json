from json import loads
from os import environ, path

from django.core.exceptions import ImproperlyConfigured

SETTINGS_DIR = environ.get('SETTINGS_DIR', path.dirname(__file__))

with open(path.join(SETTINGS_DIR, 'settings.json')) as file_handler:
    settings = loads(file_handler.read())


def get_setting(setting, settings_json=settings):
    """
    Get the setting variable or return explicit exception
    """

    try:
        return settings_json[setting]
    except KeyError:
        error_message = "Set the {setting} environment variable on settings.json".format(setting=setting)
        raise ImproperlyConfigured(error_message)
