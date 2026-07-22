from datetime import datetime


APP_NAME = "TrendHunter AI"
VERSION = "0.1.0"


def main() -> None:
    print("=" * 45)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print(f"Started: {datetime.now():%d.%m.%Y %H:%M:%S}")
    print("Status: running")
    print("=" * 45)


if __name__ == "__main__":
    main()