# === Stage 4: Редактирование записей ===
# Project: LaundryPlan
def can_update_field(loading, field, new_value):
    """Проверяет, допустимо ли изменение указанного поля загрузки."""
    if field not in ("name", "fabric", "temperature", "date"):
        return False
    if field == "name":
        return isinstance(new_value, str) and new_value.strip() != ""
    if field == "fabric":
        return isinstance(new_value, str) and new_value.strip() != ""
    if field == "temperature":
        return isinstance(new_value, int) and 30 <= new_value <= 95
    if field == "date":
        return isinstance(new_value, str) and new_value.strip() != ""
    return False


def update_loading(loading, field, new_value):
    """Редактирует допустимое поле загрузки по её идентификатору."""
    if not isinstance(loading, dict) or "id" not in loading:
        raise ValueError("Загрузка не имеет идентификатора")
    if not can_update_field(loading, field, new_value):
        raise ValueError(f"Недопустимое значение для поля '{field}'")
    setattr(loading, field, new_value)
    return loading
