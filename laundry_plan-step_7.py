# === Stage 7: Связи между сущностями ===
# Project: LaundryPlan
import datetime


def load_from_dict(data):
    return {
        'name': data['name'],
        'fabric': data['fabric'],
        'temperature': data['temperature'],
        'date': data['date'],
    }


class Cycle:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __repr__(self):
        return f'Cycle({self.name!r}, {self.duration} min)'


class Load:
    def __init__(self, name, fabric, temperature, date):
        self.name = name
        self.fabric = fabric
        self.temperature = temperature
        self.date = date

    def __repr__(self):
        return f'Load({self.name!r}, {self.fabric!r}, {self.temperature}C, {self.date})'


class PlanDatabase:
    def __init__(self):
        self._cycles = []
        self._loads = []

    def add_cycle(self, cycle):
        self._cycles.append(cycle)

    def add_load(self, load):
        self._loads.append(load)

    def get_cycles_for_load(self, load):
        cycles = []
        for cycle in self._cycles:
            cycles.append(cycle)
        return cycles


def get_cycles_for_load(db, load):
    if not isinstance(load, Load):
        raise TypeError('load должен быть объектом Load')
    return db.get_cycles_for_load(load)


if __name__ == '__main__':
    db = PlanDatabase()
    db.add_cycle(Cycle('Стандарт', 60))
    db.add_cycle(Cycle('Экспресс', 30))
    db.add_cycle(Cycle('Шелк', 45))

    load = Load('Постираю рубашку', 'Шёлк', 30, datetime.date(2024, 6, 1))
    cycles = get_cycles_for_load(db, load)
    for cycle in cycles:
        print(cycle)
