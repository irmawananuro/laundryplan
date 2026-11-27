# === Stage 11: Текстовый поиск ===
# Project: LaundryPlan
def highlight_loads(query, loads):
    query = query.strip().lower()
    if not query:
        return loads
    def render_load(load):
        text = f"[{load['name']}]"
        for field in ("fabric", "temperature", "date"):
            text += f" | {field}={load[field]}"
        parts = []
        for token in re.split(r"(\w+)", text):
            if token and token.lower() == query:
                parts.append(f"<mark>{token}</mark>")
            else:
                parts.append(token)
        return "".join(parts)
    return "\n".join(render_load(load) for load in loads)


if __name__ == "__main__":
    sample = [
        {"name": "Хлопок", "fabric": "Хлопок", "temperature": 40, "date": "2024-06-01"},
        {"name": "Шёлк", "fabric": "Шёлк", "temperature": 30, "date": "2024-06-02"},
        {"name": "Лён", "fabric": "Лён", "temperature": 60, "date": "2024-06-03"},
    ]
    for q in ("хлоп", "ш", "40", "60"):
        print(f"Поиск: {q!r}")
        print(highlight_loads(q, sample))
        print("-" * 40)
