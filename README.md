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
# 3. Customer User Model
1. `model.py`
```
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
```
2. `settings.py`
```
...
AUTH_USER_MODEL = 'app.CustomUser'
```