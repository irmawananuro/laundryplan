# === Stage 8: Генерация идентификаторов ===
# Project: LaundryPlan
import uuid

PROJECT_PREFIX = "laundryplan"


class IdentifierError(Exception):
    pass


def generate_uuid() -> str:
    return str(uuid.uuid4())


def make_unique_identifier(prefix: str) -> str:
    counter = 0
    while True:
        candidate = f"{prefix}-{generate_uuid()}-{counter}"
        if candidate not in ID_REGISTRY:
            ID_REGISTRY[candidate] = True
            return candidate
        counter += 1


ID_REGISTRY: set[str] = set()
