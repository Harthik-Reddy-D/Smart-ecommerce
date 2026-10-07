# Smart E-Commerce Platform

Complete Django 5 e-commerce reference application using PostgreSQL, Django REST Framework, Simple JWT, Auth0/social-auth, Stripe Checkout/webhooks, Channels/Redis, SMTP, Tailwind CDN, Chart.js, CSV and ReportLab PDF reports.

## 1. Local setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env   # Windows
# cp .env.example .env  # Linux/macOS
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and `/admin/`.

## 2. Docker

```bash
copy .env.example .env
# edit .env and set SECRET_KEY and service credentials
docker compose up --build
```

## 3. Daphne

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python -m daphne -b 127.0.0.1 -p 8000 config.asgi:application
```

## 4. Stripe CLI

Install Stripe CLI, authenticate, then:

```bash
stripe listen --forward-to localhost:8000/payments/webhook/
```

Copy the displayed `whsec_...` value into `STRIPE_WEBHOOK_SECRET` in `.env` and restart Django. Use Stripe test cards such as `4242 4242 4242 4242` with any future expiry and CVC.

## 5. Auth0

Create an Auth0 application, set the callback URL to `http://localhost:8000/oauth/complete/auth0/`, configure the application domain/client ID/client secret in `.env`, and enable the Auth0 connection(s) you want to expose. Auth0 handles Google/Facebook federation when those social connections are enabled in Auth0.

## 6. API

JWT token:

`POST /api/accounts/token/` with `email` and `password`.

Refresh:

`POST /api/accounts/token/refresh/`.

Products:

`GET /api/` and `GET /api/<id>/`.

Cart:

`GET /cart/api/`, `POST /cart/api/add/`, `PATCH /cart/api/<id>/`, `DELETE /cart/api/<id>/delete/`.

Checkout:

`POST /orders/api/checkout/` returns a Stripe Checkout URL.

Orders:

`GET /orders/api/` and `GET /orders/api/<id>/`.

## 7. Tests

```bash
pytest
```

## Manual checklist

1. Register a customer.
2. Log in and verify session authentication.
3. Create a category/product in admin.
4. Search/filter products.
5. Add a product to cart.
6. Attempt to exceed stock and verify rejection.
7. Start Stripe checkout.
8. Complete a test payment.
9. Verify the webhook changes payment/order status.
10. Verify an in-app notification and email backend output.
11. Open the notification WebSocket while logged in.
12. Change an order status in admin and verify the notification.
13. Log in as staff and open `/dashboard/`.
14. Verify revenue chart, top products, low-stock alerts, CSV and PDF exports.
15. Verify customer cannot access staff-only API endpoints.
