# === Stage 6: Связанная сущность ===
# Project: LaundryPlan
from datetime import date


class Cycle:
    def __init__(self, name, duration_minutes, temperature):
        self.name = name
        self.duration_minutes = duration_minutes
        self.temperature = temperature

    def __repr__(self):
        return f"Cycle(name={self.name!r}, duration_minutes={self.duration_minutes}, temperature={self.temperature})"


class LaundryPlan:
    def __init__(self):
        self._cycles = {}

    def add_cycle(self, cycle):
        key = id(cycle)
        self._cycles[key] = cycle
        return key


def create_cycle(name, duration_minutes, temperature):
    return Cycle(name, duration_minutes, temperature)
