# django-settings-json

Sample `settings.json` file:

```json
{
  "DEBUG": true, 
  "TIME_ZONE": "America/New_York"
}
```

Usage
--

Use `get_setting()` when retrieving environment variables on your `settings.py` file:

```python
from settings_json import get_setting

DEBUG = get_setting('DEBUG')
TIME_ZONE = get_setting('TIME_ZONE')
```

GitIgnore
--

Remember to add `settings.json` into your `.gitignore`, so it don't get tracked.

```
settings.json
```

Missing Variables
--

If you forget to add a variable on your `settings.json`, it'll raise an error like the one below:

`Set the TIME_ZONE environment variable on settings.json`
