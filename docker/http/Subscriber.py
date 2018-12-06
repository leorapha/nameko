from nameko.events import event_handler


class SubscriberTest:

    name = "subscriber"

    @event_handler("publisher", "event")
    def handle_event(self, payload):
        print("subscriber received:", payload)
