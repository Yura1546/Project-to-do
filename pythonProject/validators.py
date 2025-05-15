import datetime
MAX_DESCRIPTION_LENGTH = 100
MIN_PRIORITY = 1
MAX_PRIORITY = 5

def validate_date(date_str: str) -> datetime.date:
   """
   Перевіряє коректність формату дати та повертає обʼєкт дати.
   Якщо формат неправильний, викликає помилку ValueError.
   """
   try:
       date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
       return date
   except ValueError:
       raise ValueError(
           f"Невірний формат дати: {date_str}. Використовуйте YYYY-MM-DD."
       )

def validate_description(description: str) -> None:
   """
   Перевіряє, що опис завдання не пустий і не перевищує максимальної довжини.
   Викликає помилку ValueError при невідповідності.
   """
   if not description.strip():
       raise ValueError("Опис завдання не може бути пустим.")
   if len(description) > MAX_DESCRIPTION_LENGTH:
       raise ValueError(
           f"Опис завдання не може бути довшим за "
           f"{MAX_DESCRIPTION_LENGTH} символів."
       )


def validate_priority(priority: int) -> None:
   """
   Перевіряє, що пріоритет є цілим числом в допустимих межах.
   Викликає помилку ValueError при невідповідності.
   """
   if not isinstance(priority, int):
       raise ValueError("Пріоритет має бути цілим числом.")
   if priority < MIN_PRIORITY or priority > MAX_PRIORITY:
       raise ValueError(
           f"Пріоритет має бути в межах від {MIN_PRIORITY} до {MAX_PRIORITY}."
       )
