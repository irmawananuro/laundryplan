# === Stage 2: Проверка полей ===
# Project: LaundryPlan
import datetime


def normalize_text(value):
    if value is None:
        return ""
    return " ".join(str(value).strip().split()).strip()


def normalize_temperature(value):
    if value is None:
        return None
    text = str(value).strip().lower()
    mapping = {"холодная": 30, "тёплая": 40, "тёплая": 40,
               "горячая": 60, "деликатная": 30}
    if text in mapping:
        return mapping[text]
    number = text.replace(",", ".").replace("%", "")
    if number.isdigit():
        return float(number)
    return None


def normalize_date(value):
    if value is None:
        return None
    text = str(value).strip()
    formats = ("%d.%m.%Y", "%Y-%m-%d", "%m/%d/%Y",
               "%d-%m-%Y", "%Y.%m.%d")
    for fmt in formats:
        try:
            return datetime.datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return None


def validate_load(text, fabric, temperature, date):
    errors = []

    name = normalize_text(text)
    if not name:
        errors.append("Название загрузки не может быть пустым.")

    fabric = normalize_text(fabric)
    if not fabric:
        errors.append("Укажите тип ткани для загрузки.")

    temperature = normalize_temperature(temperature)
    if temperature is None:
        errors.append("Неверная температура. Ожидаются значения: 30, 40, 60 или слова 'холодная', 'тёплая', 'горячая'.")
    elif temperature < 0 or temperature > 95:
        errors.append("Температура должна быть в диапазоне от 0 до 95 градусов.")

    date = normalize_date(date)
    if date is None:
        errors.append("Неверный формат даты. Используйте формат DD.MM.YYYY.")

    if errors:
        return None, errors

    return {
        "name": name,
        "fabric": fabric,
        "temperature": temperature,
        "date": date,
    }, []
