from task_list import TaskList
from task import Task
import validators

class TaskManager:
    """
    Менеджер завдань, який зберігає та управляє кількома списками завдань.
    Забезпечує створення, редагування, видалення завдань, а також
    фільтрацію і сортування у межах активного списку.
    """

    def __init__(self):
        """
        Ініціалізує TaskManager із пустим словником списків завдань,
        лічильником ID та активним списком.
        """
        self.task_lists = {}
        self.active_list_name = None
        self._next_id = 1

    def create_task_list(self, name: str):
        """
        Створює новий список завдань із унікальною назвою
        і робить його активним.
        """
        if name in self.task_lists:
            raise ValueError(f"Список з назвою '{name}' вже існує.")
        self.task_lists[name] = TaskList()
        self.active_list_name = name

    def switch_task_list(self, name: str):
        """
        Перемикає активний список завдань на існуючий за назвою.
        """
        if name not in self.task_lists:
            raise ValueError(f"Список з назвою '{name}' не знайдено.")
        self.active_list_name = name

    def get_active_list(self) -> TaskList:
        """
        Повертає активний список завдань.
        """
        if not self.active_list_name:
            raise ValueError("Активний список не вибрано.")
        return self.task_lists[self.active_list_name]

    def create_task(self, description: str, date_str: str, priority: int) -> Task:
        """
        Створює нове завдання у активному списку після валідації.

        """
        validators.validate_description(description)
        due_date = validators.validate_date(date_str)
        validators.validate_priority(priority)

        task = Task(
            id=self._next_id,
            description=description,
            due_date=due_date,
            priority=priority
        )
        self.get_active_list().add(task)
        self._next_id += 1
        return task

    def delete_task(self, task_id: int):
        """
        Видаляє завдання за ID з активного списку.

        """
        self.get_active_list().remove(task_id)

    def complete_task(self, task_id: int):
        """
        Позначає завдання як виконане у активному списку.

        """
        task = self.get_active_list().get(task_id)
        if task:
            task.mark_completed()

    def update_task(self, task_id: int, description=None, date_str=None, priority=None):
        """
        """
        task = self.get_active_list().get(task_id)
        if not task:
            return

        if description is not None:
            validators.validate_description(description)
        due_date = validators.validate_date(date_str) if date_str else None
        if priority is not None:
            validators.validate_priority(priority)

        task.update(description, due_date, priority)

    def list_tasks(self, sort_by: str = None):
        """
        Повертає список завдань із активного списку,
        опційно відсортований за датою або пріоритетом.

        """
        return self.get_active_list().list_all(sort_by)

    def filter_tasks(self, status: str = None, priority: int = None):
        """
        Фільтрує завдання активного списку за статусом
        або пріоритетом.

        """
        if status in ('active', 'completed'):
            completed = (status == 'completed')
            return self.get_active_list().filter_by_status(completed)

        if priority is not None:
            return self.get_active_list().filter_by_priority(priority)

        return []

    def rename_task_list(self, old_name: str, new_name: str):
        """
        Перейменовує список завдань із назви old_name у new_name.
        """
        if old_name not in self.task_lists:
            raise ValueError(f"Список з назвою '{old_name}' не знайдено.")
        if new_name in self.task_lists:
            raise ValueError(f"Список з назвою '{new_name}' вже існує.")

        self.task_lists[new_name] = self.task_lists.pop(old_name)

        if self.active_list_name == old_name:
            self.active_list_name = new_name
