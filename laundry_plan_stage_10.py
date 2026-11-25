# === Stage 10: Сортировка записей ===
# Project: LaundryPlan
from datetime import datetime


def sort_loads_by_name_desc(records):
    return sorted(records, key=lambda r: r["name"], reverse=True)


def sort_loads_by_name_asc(records):
    return sorted(records, key=lambda r: r["name"])


def sort_loads_by_date_desc(records):
    return sorted(
        records,
        key=lambda r: r["created_at"],
        reverse=True,
    )


def sort_loads_by_date_asc(records):
    return sorted(records, key=lambda r: r["created_at"])


def sort_loads(records, field="name", order="asc"):
    reverse = order == "desc"
    return sorted(records, key=lambda r: r[field], reverse=reverse)


if __name__ == "__main__":
    sample = [
        {"name": "Полотенца", "created_at": datetime(2025, 1, 3)},
        {"name": "Деликатное", "created_at": datetime(2025, 1, 1)},
        {"name": "Бельё", "created_at": datetime(2025, 1, 2)},
    ]

    print("По названию (по возрастанию):")
    for r in sort_loads(sample, "name", "asc"):
        print(" ", r["name"])

    print("По названию (по убыванию):")
    for r in sort_loads(sample, "name", "desc"):
        print(" ", r["name"])

    print("По дате создания (по возрастанию):")
    for r in sort_loads(sample, "created_at", "asc"):
        print(" ", r["name"])

    print("По дате создания (по убыванию):")
    for r in sort_loads(sample, "created_at", "desc"):
        print(" ", r["name"])
