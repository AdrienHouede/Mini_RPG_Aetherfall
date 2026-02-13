class ObjectAction:
    def __init__(self, user, item):
        self.user = user
        self.item = item

    def execute(self):
        old_value = getattr(self.user, self.item.type if self.item.type != "heal" else "hp")
        self.user.use_item(self.item)
        new_value = getattr(self.user, self.item.type if self.item.type != "heal" else "hp")
        return {
            "user": self.user.__class__.__name__,
            "item": self.item.name,
            "stat": self.item.type if self.item.type != "heal" else "hp",
            "change": new_value - old_value
        }