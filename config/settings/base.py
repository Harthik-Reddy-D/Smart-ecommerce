from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv
BASE_DIR=Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR/".env")
def env_bool(k,d=False): return os.getenv(k,str(d)).lower() in {"1","true","yes","on"}
def env_list(k,d=""): return [x.strip() for x in os.getenv(k,d).split(",") if x.strip()]
SECRET_KEY=os.getenv("SECRET_KEY","unsafe-dev-key")
DEBUG=env_bool("DEBUG")
ALLOWED_HOSTS=env_list("ALLOWED_HOSTS","localhost,127.0.0.1")
CSRF_TRUSTED_ORIGINS=env_list("CSRF_TRUSTED_ORIGINS")
INSTALLED_APPS=["django.contrib.admin","django.contrib.auth","django.contrib.contenttypes","django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles","django.contrib.sites","rest_framework","rest_framework_simplejwt","channels","social_django","corsheaders","accounts","products","cart","orders","payments","notifications","dashboard"]
MIDDLEWARE=["django.middleware.security.SecurityMiddleware","corsheaders.middleware.CorsMiddleware","django.contrib.sessions.middleware.SessionMiddleware","django.middleware.common.CommonMiddleware","django.middleware.csrf.CsrfViewMiddleware","django.contrib.auth.middleware.AuthenticationMiddleware","django.contrib.messages.middleware.MessageMiddleware","django.middleware.clickjacking.XFrameOptionsMiddleware"]
ROOT_URLCONF="config.urls"
TEMPLATES=[{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[BASE_DIR/"templates"],"APP_DIRS":True,"OPTIONS":{"context_processors":["django.template.context_processors.request","django.contrib.auth.context_processors.auth","django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION="config.wsgi.application"
ASGI_APPLICATION="config.asgi.application"
DATABASES={"default":{"ENGINE":"django.db.backends.postgresql","NAME":os.getenv("POSTGRES_DB","smart_ecommerce"),"USER":os.getenv("POSTGRES_USER","smartshop"),"PASSWORD":os.getenv("POSTGRES_PASSWORD","smartshop_password"),"HOST":os.getenv("POSTGRES_HOST","localhost"),"PORT":os.getenv("POSTGRES_PORT","5432"),"CONN_MAX_AGE":60}}
AUTH_PASSWORD_VALIDATORS=[{"NAME":"django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},{"NAME":"django.contrib.auth.password_validation.MinimumLengthValidator","OPTIONS":{"min_length":10}},{"NAME":"django.contrib.auth.password_validation.CommonPasswordValidator"},{"NAME":"django.contrib.auth.password_validation.NumericPasswordValidator"}]
LANGUAGE_CODE="en-us"; TIME_ZONE="Asia/Kolkata"; USE_I18N=True; USE_TZ=True
STATIC_URL="/static/"; STATIC_ROOT=BASE_DIR/"staticfiles"; STATICFILES_DIRS=[BASE_DIR/"static"]; MEDIA_URL="/media/"; MEDIA_ROOT=BASE_DIR/"media"
STORAGES={"default":{"BACKEND":"django.core.files.storage.FileSystemStorage"},"staticfiles":{"BACKEND":"django.contrib.staticfiles.storage.ManifestStaticFilesStorage"}}
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
AUTH_USER_MODEL="accounts.User"
LOGIN_URL="accounts:login"; LOGIN_REDIRECT_URL="/"; LOGOUT_REDIRECT_URL="/"
SITE_ID=1
REST_FRAMEWORK={"DEFAULT_AUTHENTICATION_CLASSES":["rest_framework_simplejwt.authentication.JWTAuthentication","rest_framework.authentication.SessionAuthentication"],"DEFAULT_PERMISSION_CLASSES":["rest_framework.permissions.IsAuthenticated"],"DEFAULT_PAGINATION_CLASS":"rest_framework.pagination.PageNumberPagination","PAGE_SIZE":12,"DEFAULT_THROTTLE_CLASSES":["rest_framework.throttling.AnonRateThrottle","rest_framework.throttling.UserRateThrottle"],"DEFAULT_THROTTLE_RATES":{"anon":"60/minute","user":"300/minute"}}
SIMPLE_JWT={"ACCESS_TOKEN_LIFETIME":timedelta(minutes=30),"REFRESH_TOKEN_LIFETIME":timedelta(days=7),"ROTATE_REFRESH_TOKENS":True,"BLACKLIST_AFTER_ROTATION":True,"UPDATE_LAST_LOGIN":True,"ALGORITHM":"HS256","SIGNING_KEY":SECRET_KEY,"AUTH_HEADER_TYPES":("Bearer",)}
REDIS_URL=os.getenv("REDIS_URL","redis://localhost:6379/1")
CHANNEL_LAYERS={"default":{"BACKEND":"channels_redis.core.RedisChannelLayer","CONFIG":{"hosts":[REDIS_URL]}}}
AUTHENTICATION_BACKENDS=["django.contrib.auth.backends.ModelBackend","social_core.backends.auth0.Auth0OAuth2"]
SOCIAL_AUTH_AUTH0_KEY=os.getenv("AUTH0_CLIENT_ID",""); SOCIAL_AUTH_AUTH0_SECRET=os.getenv("AUTH0_CLIENT_SECRET",""); SOCIAL_AUTH_AUTH0_DOMAIN=os.getenv("AUTH0_DOMAIN",""); SOCIAL_AUTH_AUTH0_SCOPE=["openid","profile","email"]
SOCIAL_AUTH_AUTH0_USE_BASIC_AUTH = True
SOCIAL_AUTH_URL_NAMESPACE="social"; SOCIAL_AUTH_LOGIN_REDIRECT_URL="/"; SOCIAL_AUTH_LOGIN_ERROR_URL="/accounts/login/"; SOCIAL_AUTH_RAISE_EXCEPTIONS=False
SOCIAL_AUTH_PIPELINE=["social_core.pipeline.social_auth.social_details","social_core.pipeline.social_auth.social_uid","social_core.pipeline.social_auth.auth_allowed","social_core.pipeline.social_auth.social_user","accounts.social.create_social_user","social_core.pipeline.social_auth.associate_user","social_core.pipeline.social_auth.load_extra_data","social_core.pipeline.user.user_details"]
CORS_ALLOWED_ORIGINS=env_list("CORS_ALLOWED_ORIGINS"); CORS_ALLOW_CREDENTIALS=True
CSRF_COOKIE_HTTPONLY=True; SESSION_COOKIE_HTTPONLY=True; SESSION_COOKIE_SAMESITE="Lax"; CSRF_COOKIE_SAMESITE="Lax"
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"; EMAIL_HOST=os.getenv("EMAIL_HOST",""); EMAIL_PORT=int(os.getenv("EMAIL_PORT","587")); EMAIL_USE_TLS=env_bool("EMAIL_USE_TLS",True); EMAIL_HOST_USER=os.getenv("EMAIL_HOST_USER",""); EMAIL_HOST_PASSWORD=os.getenv("EMAIL_HOST_PASSWORD",""); DEFAULT_FROM_EMAIL=os.getenv("DEFAULT_FROM_EMAIL","Smart E-Commerce <noreply@example.com>")
STRIPE_SECRET_KEY=os.getenv("STRIPE_SECRET_KEY",""); STRIPE_PUBLISHABLE_KEY=os.getenv("STRIPE_PUBLISHABLE_KEY",""); STRIPE_WEBHOOK_SECRET=os.getenv("STRIPE_WEBHOOK_SECRET",""); STRIPE_SUCCESS_URL=os.getenv("STRIPE_SUCCESS_URL","http://localhost:8000/payments/success/"); STRIPE_CANCEL_URL=os.getenv("STRIPE_CANCEL_URL","http://localhost:8000/payments/cancel/")
SITE_URL=os.getenv("SITE_URL","http://localhost:8000")
SECURE_PROXY_SSL_HEADER=("HTTP_X_FORWARDED_PROTO","https"); SECURE_SSL_REDIRECT=env_bool("SECURE_SSL_REDIRECT"); SESSION_COOKIE_SECURE=env_bool("SESSION_COOKIE_SECURE"); CSRF_COOKIE_SECURE=env_bool("CSRF_COOKIE_SECURE"); SECURE_CONTENT_TYPE_NOSNIFF=True; X_FRAME_OPTIONS="DENY"; SECURE_REFERRER_POLICY="same-origin"
LOGGING={"version":1,"disable_existing_loggers":False,"handlers":{"console":{"class":"logging.StreamHandler"}},"root":{"handlers":["console"],"level":"INFO"}}
