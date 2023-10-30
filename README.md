# Student_Mgmt_system

# 1. Initial Setup

1. `django-admin startproject sms .`
2. `python3 manage.py startapp app`
3. `create 'templates' and 'static' directories in root`
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

# 2. Basic Setup
1. `Create Directories`
```
create 'app/templates/app/Hod'
create 'app/templates/app/Staff'
create 'app/templates/app/Student'
```
2. `Create Files`
```
app/Hod_Views.py
app/Staff_Views.py
app/Student_Views.py
```
