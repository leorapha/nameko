from nameko.events import EventDispatcher
from nameko.rpc import rpc


class TestPublish:
    name = "publisher"

    dispatch = EventDispatcher()

    @rpc
    def send_message(self, payload):
        self.dispatch("event", payload)