import datetime
import requests


def main():
  print("=== DevOps Python App in Docker ===")
  print(f"Текущее время: {datetime.datetime.now()}")

  try:
    response = requests.get(
        "https://api.exchangerate-api.com/v4/latest/USD"
    )
    if response.status_code == 200:
      data = response.json()
      kzt = data["rates"].get("KZT", "N/A")
      rub = data["rates"].get("RUB", "N/A")
      print(f"Курс USD к KZT: {kzt}")
      print(f"Курс USD к RUB: {rub}")
    else:
      print("Не удалось получить данные API")
  except Exception as e:
    print(f"Ошибка при выполнении запроса: {e}")


if __name__ == "__main__":
  main()