import pytest
from channels.testing import WebsocketCommunicator
from django.test import override_settings
from config.asgi import application
@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test_websocket_rejects_anonymous():
 communicator=WebsocketCommunicator(application,"/ws/notifications/"); connected,_=await communicator.connect(); assert not connected; await communicator.disconnect()
