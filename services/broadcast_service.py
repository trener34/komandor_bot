class BroadcastService:
    def __init__(self):
        self.subscribers = set()

    def subscribe(self, user_id):
        self.subscribers.add(user_id)

    def unsubscribe(self, user_id):
        self.subscribers.discard(user_id)

    def get_subscribers(self):
        return list(self.subscribers)
