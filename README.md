# Student_Mgmt_system

1. `django-admin startproject sms .`
2. `python3 manage.py startapp app`
3. `settings.py`
```
TEMPLATES = [
    {
        ...
        "DIRS": [BASE_DIR, "templates"],
        ...
    },
]

STATIC_URL = "static/"
STATIC_ROOT = "/static/"

STATICFILES_DIRS = [BASE_DIR, "static"]
```
4. `urls.py (project)`
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```