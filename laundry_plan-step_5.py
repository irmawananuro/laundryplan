# === Stage 5: Удаление и восстановление ===
# Project: LaundryPlan
from datetime import date


class Load:
    def __init__(self, name, fabric, temperature, scheduled_date):
        self.id = None
        self.name = name
        self.fabric = fabric
        self.temperature = temperature
        self.scheduled_date = scheduled_date
        self.deleted = False

    def mark_deleted(self):
        self.deleted = True

    def restore(self):
        self.deleted = False


class LoadStore:
    def __init__(self):
        self._items = {}
        self._counter = 0

    def add(self, name, fabric, temperature, scheduled_date):
        load = Load(name, fabric, temperature, scheduled_date)
        load.id = self._counter
        self._counter += 1
        self._items[load.id] = load
        return load

    def get(self, load_id):
        return self._items.get(load_id)

    def list_active(self):
        return [item for item in self._items.values() if not item.deleted]

    def list_deleted(self):
        return [item for item in self._items.values() if item.deleted]

    def remove(self, load_id):
        load = self._items.get(load_id)
        if load is not None:
            load.mark_deleted()
            return True
        return False

    def restore(self, load_id):
        load = self._items.get(load_id)
        if load is not None:
            load.restore()
            return True
        return False
