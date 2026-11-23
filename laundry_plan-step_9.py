# === Stage 9: Фильтрация записей ===
# Project: LaundryPlan
from datetime import date


def filter_by_fabric(loadings, fabric):
    if fabric is None:
        return list(loadings)
    return [load for load in loadings if load.get("ткань") == fabric]


def filter_by_date_range(loadings, start_date, end_date):
    if start_date is None and end_date is None:
        return list(loadings)
    result = []
    for load in loadings:
        load_date = load.get("дата")
        if start_date is not None and load_date < start_date:
            continue
        if end_date is not None and load_date > end_date:
            continue
        result.append(load)
    return result


def filter_loadings(loadings, fabric=None, start_date=None, end_date=None):
    filtered = loadings if fabric is None else filter_by_fabric(loadings, fabric)
    if start_date is not None or end_date is not None:
        filtered = filter_by_date_range(filtered, start_date, end_date)
    return filtered


if __name__ == "__main__":
    sample = [
        {"название": "Хлопок", "ткань": "хлопок", "температура": 30, "дата": date(2024, 1, 5)},
        {"название": "Шелк", "ткань": "шелк", "температура": 30, "дата": date(2024, 1, 10)},
        {"название": "Джинсы", "ткань": "хлопок", "температура": 40, "дата": date(2024, 1, 15)},
        {"название": "Шорты", "ткань": "синтетика", "температура": 30, "дата": date(2024, 1, 20)},
    ]
    print(filter_loadings(sample, fabric="хлопок"))
    print(filter_loadings(sample, start_date=date(2024, 1, 10), end_date=date(2024, 1, 15)))
