from dataclasses import dataclass, field
import datetime


@dataclass
class Task:
   """
   Клас, що представляє одне завдання з описом, датою, пріоритетом та статусом виконання.
   """
   id: int
   description: str
   due_date: datetime.date
   priority: int
   completed: bool = field(default=False)


   def mark_completed(self) -> None:
       """
       Позначає завдання як завершене.
       """
       self.completed = True


   def update(self, description: str = None, due_date: datetime.date = None, priority: int = None) -> None:
       """
       Оновлює атрибути завдання, якщо передані нові значення.
       """
       if description is not None:
           self.description = description
       if due_date is not None:
           self.due_date = due_date
       if priority is not None:
           self.priority = priority
