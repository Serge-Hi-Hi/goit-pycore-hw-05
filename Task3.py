import sys

def parse_log_line(line: str) -> dict:
    date, time, level, message = line.strip().split(' ', 3)

    return {
        'date': date,
        'time': time,
        'level': level,
        'message': message
    }

def load_logs(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as file:
        return [parse_log_line(line) for line in file if line.strip()]

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1

    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    for level, count in counts.items():
        print(f"{level:<17}| {count}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень]")
        return

    file_path = sys.argv[1]

    try:
        logs = load_logs(file_path)
    except (FileNotFoundError, PermissionError, UnicodeError) as e :
        print(f"Помилка читання файлу: {e}")
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)

        print(f"\nДеталі логів для рівня '{level}':")

        for log in filtered_logs:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")


if __name__ == '__main__':
    main()