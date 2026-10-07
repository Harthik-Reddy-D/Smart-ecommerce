from .base import *
DEBUG=True
ALLOWED_HOSTS=["localhost","127.0.0.1","0.0.0.0"]
EMAIL_BACKEND="django.core.mail.backends.console.EmailBackend"
STORAGES["staticfiles"]={"BACKEND":"django.contrib.staticfiles.storage.StaticFilesStorage"}
