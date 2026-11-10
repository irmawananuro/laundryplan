# === Stage 3: Хранилище в памяти ===
# Project: LaundryPlan
import time
import uuid


class Load:
    def __init__(self, name, fabric, temperature, date):
        self.id = uuid.uuid4().hex
        self.name = name
        self.fabric = fabric
        self.temperature = temperature
        self.date = date

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "fabric": self.fabric,
            "temperature": self.temperature,
            "date": self.date,
        }


class LoadStore:
    def __init__(self):
        self._items = []
        self._last_timestamp = 0

    def add(self, load):
        self._items.append(load)
        self._last_timestamp = time.time_ns()
        return load.id

    def get(self, load_id):
        for item in self._items:
            if item.id == load_id:
                return item
        return None

    def list(self):
        return list(self._items)
