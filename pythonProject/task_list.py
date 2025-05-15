from typing import List, Optional
from task import Task


class TaskList:
   """
   Клас для управління списком завдань: додавання, видалення, пошук, сортування та фільтрація.
   """


   def __init__(self):
       """
       Ініціалізує порожній список завдань.
       """
       self.tasks: List[Task] = []


   def add(self, task: Task) -> None:
       """
       Додає нове завдання до списку.
       """
       self.tasks.append(task)


   def remove(self, task_id: int) -> None:
       """
       Видаляє завдання зі списку за його id.
       """
       self.tasks = [t for t in self.tasks if t.id != task_id]


   def get(self, task_id: int) -> Optional[Task]:
       """
       Повертає завдання за id або None, якщо не знайдено.
       """
       for t in self.tasks:
           if t.id == task_id:
               return t
       return None


   def list_all(self, sort_by: str = None) -> List[Task]:
       """
       Повертає всі завдання, опціонально відсортовані за датою або пріоритетом.
       """
       if sort_by == 'date':
           return sorted(self.tasks, key=lambda t: t.due_date)
       if sort_by == 'priority':
           return sorted(self.tasks, key=lambda t: t.priority)
       return list(self.tasks)


   def filter_by_status(self, completed: bool) -> List[Task]:
       """
       Фільтрує завдання за статусом виконання.
       """
       return [t for t in self.tasks if t.completed == completed]


   def filter_by_priority(self, priority: int) -> List[Task]:
       """
       Фільтрує завдання за пріоритетом.
       """
       return [t for t in self.tasks if t.priority == priority]