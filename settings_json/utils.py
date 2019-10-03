from json import loads
from os.path import dirname, join

from django.core.exceptions import ImproperlyConfigured

SETTINGS_DIR = dirname(__file__)

with open(join(SETTINGS_DIR, 'settings.json')) as file_handler:
    settings = loads(file_handler.read())


def get_setting(setting, settings_json=settings):
    """
    Get the setting variable or return explicit exception
    """

    try:
        return settings_json[setting]
    except KeyError:
        error_message = "Set the {} environment variable on settings.json".format(setting)
        raise ImproperlyConfigured(error_message)
