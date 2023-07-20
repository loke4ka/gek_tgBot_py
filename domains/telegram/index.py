from aiogram import types
from aiogram.dispatcher import FSMContext
from ..data.index import TaskDB, Task

task_db = TaskDB('tasks.db')


async def cmd_start(message: types.Message):
    await message.answer("Дароу! Я бот для управления списком задач. Вот доступные команды:\n"
                         "/add <задача> - добавление новой задачи\n"
                         "/done <индекс> - отметка задачи с указанным индексом как выполненной\n"
                         "/list - вывод списка всех задач\n"
                         "/delete <индекс> - удаление задачи с указанным индексом из списка")


async def cmd_add(message: types.Message):
    text = message.get_args()
    if text:
        task_db.add_task(text, False)
        await message.answer(f"Задача \"{text}\" успешно добавлена!")
    else:
        await message.answer("Вы не указали текст задачи. Используйте команду /add <задача>")


async def cmd_done(message: types.Message):
    task_id = int(message.get_args())
    task = task_db.get_task_by_id(task_id)
    if task:
        task_db.update_task(task_id, task.task, True)
        await message.answer(f"Задача \"{task.task}\" выполнена!")
    else:
        await message.answer("Задача с указанным индексом не найдена. Проверьте правильность ввода.")


async def cmd_list(message: types.Message):
    tasks = task_db.get_all_tasks()
    if tasks:
        task_list = "\n".join(
            [f"{task.task_id}. {'[x]' if task.is_done else '[ ]'} {task.task} ({task.date})" for task in tasks])
        await message.answer(f"Список задач:\n{task_list}")
    else:
        await message.answer("Список задач пуст. Используйте команду /add <задача>, чтобы добавить новую задачу.")


async def cmd_delete(message: types.Message):
    task_id = int(message.get_args())
    task = task_db.get_task_by_id(task_id)
    if task:
        task_db.delete_task(task_id)
        await message.answer(f"Задача \"{task.task}\" успешно удалена!")
    else:
        await message.answer("Задача с указанным индексом не найдена. Проверьте правильность ввода.")
