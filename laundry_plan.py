# === Stage 1: Каркас модуля ===
# Project: LaundryPlan
from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Load:
    name: str
    fabric: str
    temperature: int
    wash_day: date


def create_demo_loads():
    today = date.today()
    return [
        Load("Постельное белье", "Хлопок", 40, today),
        Load("Джинсы", "Деним", 30, today),
        Load("Шерстяной свитер", "Шерсть", 30, today + timedelta(days=1)),
        Load("Синтетические рубашки", "Полиэстер", 40, today + timedelta(days=1)),
        Load("Кухонные полотенца", "Хлопок", 60, today + timedelta(days=2)),
    ]


def main():
    loads = create_demo_loads()
    print("LaundryPlan — планировщик стирки")
    print("=" * 30)
    for index, load in enumerate(loads, start=1):
        print(f"{index}. {load.name}")
        print(f"   Ткань:    {load.fabric}")
        print(f"   Температура: {load.temperature}°C")
        print(f"   Дата:    {load.wash_day.isoformat()}")
        print("-" * 30)


if __name__ == "__main__":
    main()
