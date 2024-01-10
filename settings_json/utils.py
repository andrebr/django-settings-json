from json import loads
from os import environ, path
from traceback import extract_stack

from django.core.exceptions import ImproperlyConfigured

SETTINGS_DIR = environ.get('SETTINGS_DIR')


def get_settings_dir_from_traceback():
    for file, _, _, _ in extract_stack():
        if file.endswith('/settings.py'):
            return path.dirname(file)


if not SETTINGS_DIR:
    SETTINGS_DIR = get_settings_dir_from_traceback()

with open(path.join(SETTINGS_DIR, 'settings.json')) as file_handler:
    settings = loads(file_handler.read())


def get_setting(setting, settings_json=settings):
    """
    Get the setting variable or return explicit exception
    """

    try:
        return settings_json[setting]
    except KeyError:
        error_message = f"Set the {setting} environment variable on settings.json"
        raise ImproperlyConfigured(error_message)
