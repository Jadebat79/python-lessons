logs = [
  "2024-08-04 12:00:00 [INFO] System started",
  "2024-08-04 12:05:23 [ERROR] Failed to connect",
  "2024-08-04 12:10:45 [WARNING] Low memory",
  "2024-08-04 12:12:00 [ERROR] Timeout on request"
]

def filter_errors(logs: list[str], level: str) -> list[str]:
    filtered = []

    target = f"[{level}]"

    for line in logs:
        if target in line:
            filtered.append(line)

    return filtered


print(filter_errors(logs, "ERROR"))
