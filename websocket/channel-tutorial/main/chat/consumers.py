import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # join group channel
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        json_data = json.loads(text_data)
        message = json_data["message"]
        event = {"type": "chat_message", "message": message}
        await self.channel_layer.group_send(self.room_group_name, event)

    async def chat_message(self, event):
        message = event["message"]
        response = json.dumps({"message": message})
        await self.send(text_data=response)
