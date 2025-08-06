logs = [
  "2024-08-04 12:00:00 [INFO] System started",
  "2024-08-04 12:05:23 [ERROR] Failed to connect",
  "2024-08-04 12:10:45 [WARNING] Low memory",
  "2024-08-04 12:12:00 [ERROR] Timeout on request",
  "2024-08-04 12:15:00 [INFO] Shutdown complete"
]

def count_log_levels(logs: list[str]) -> dict[str, int]:
    counts = {}

    # target = f"[{level}]"

    for line in logs:
        start = line.find('[') + 1
        end = line.find(']')
        level = line[start:end]

        if level in counts:
            counts [level] += 1
        else:
            counts[level] = 1

    return counts
