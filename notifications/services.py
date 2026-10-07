from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.core.mail import send_mail
from .models import Notification
def create_notification(user, kind, message, email=True, order=None):
    n = Notification.objects.create(
        user=user,
        order=order,
        type=kind,
        message=message,
    )

    channel = get_channel_layer()
    async_to_sync(channel.group_send)(
        f"user_{user.id}",
        {
            "type": "notification.message",
            "message": message,
            "notification_id": n.id,
            "kind": kind,
        },
    )

    if email:
        send_mail(
            "Smart E-Commerce Notification",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=True,
        )

    return n

def notify_order_status(order, old_status=None):
    return create_notification(
        order.user,
        "order_status",
        f"Order #{order.id} status changed to {order.get_order_status_display()}.",
        order=order,
    )
