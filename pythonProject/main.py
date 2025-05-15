from task_manager import TaskManager

MENU = '''
Виберіть дію:
0. Вихід
1. Створити новий список завдань
2. Перемкнути активний список завдань
3. Показати назву активного списку
4. Додати завдання
5. Видалити завдання
6. Позначити як завершене
7. Показати всі завдання
8. Показати відфільтровані завдання
9. Оновити завдання
10. Перейменувати список завдань
>>> '''

def main():
    manager = TaskManager()

    while True:
        choice = input(MENU).strip()

        if choice == '0':
            break

        elif choice == '1':
            name = input('Назва нового списку завдань: ').strip()
            try:
                manager.create_task_list(name)
                print(f"Список '{name}' створено і активовано.")
            except ValueError as e:
                print(e)

        elif choice == '2':
            name = input('Назва списку для активації: ').strip()
            try:
                manager.switch_task_list(name)
                print(f"Активний список тепер: '{name}'.")
            except ValueError as e:
                print(e)

        elif choice == '3':
            try:
                print(f"Активний список: '{manager.active_list_name}'")
            except Exception:
                print("Активний список не вибрано.")

        elif choice == '4':
            if not manager.active_list_name:
                print("Спочатку створіть або виберіть список завдань.")
                continue
            desc = input('Опис: ')
            date = input('Дата (YYYY-MM-DD): ')
            pr = input('Пріоритет (1-5): ')
            try:
                pr = int(pr)
                task = manager.create_task(desc, date, pr)
                print(f'Завдання {task.id} створено у списку "{manager.active_list_name}".')
            except Exception as e:
                print(f"Помилка створення завдання: {e}")

        elif choice == '5':
            if not manager.active_list_name:
                print("Спочатку виберіть активний список.")
                continue
            tid = input('ID завдання для видалення: ')
            try:
                tid = int(tid)
                manager.delete_task(tid)
                print('Завдання видалено.')
            except Exception as e:
                print(f"Помилка видалення: {e}")

        elif choice == '6':
            if not manager.active_list_name:
                print("Спочатку виберіть активний список.")
                continue
            tid = input('ID завершеного завдання: ')
            try:
                tid = int(tid)
                manager.complete_task(tid)
                print('Завдання позначено як завершене.')
            except Exception as e:
                print(f"Помилка: {e}")

        elif choice == '7':
            if not manager.active_list_name:
                print("Спочатку виберіть активний список.")
                continue
            sort = input('Сортувати? (date/priority/none): ')
            tasks = manager.list_tasks(sort if sort != 'none' else None)
            if tasks:
                for t in tasks:
                    print(t)
            else:
                print("Завдань немає.")

        elif choice == '8':
            if not manager.active_list_name:
                print("Спочатку виберіть активний список.")
                continue
            status = input('Статус (active/completed) або пусто: ').strip()
            pr = input('Пріоритет (1-5) або пусто: ').strip()
            try:
                pr_val = int(pr) if pr else None
                res = manager.filter_tasks(status or None, pr_val)
                if res:
                    for t in res:
                        print(t)
                else:
                    print("Немає завдань, що відповідають критеріям.")
            except Exception as e:
                print(f"Помилка фільтрації: {e}")

        elif choice == '9':
            if not manager.active_list_name:
                print("Спочатку виберіть активний список.")
                continue
            tid = input('ID для оновлення: ')
            desc = input('Новий опис або пусто: ')
            date = input('Нова дата (YYYY-MM-DD) або пусто: ')
            pr = input('Новий пріоритет (1-5) або пусто: ')
            try:
                tid = int(tid)
                pr_val = int(pr) if pr else None
                manager.update_task(tid, description=desc or None,
                 date_str=date or None,
                priority=pr_val)
                print('Оновлено.')
            except Exception as e:
                print(f"Помилка оновлення: {e}")

        elif choice == '10':
            old_name = input('Поточна назва списку: ').strip()
            new_name = input('Нова назва списку: ').strip()
            try:
                manager.rename_task_list(old_name, new_name)
                print(f"Список '{old_name}' перейменовано на '{new_name}'.")
            except ValueError as e:
                print(e)

        else:
            print('Невірний вибір.')

if __name__ == '__main__':
    main()
