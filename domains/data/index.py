from dataclasses import dataclass
from typing import List
from datetime import datetime

from domains.db.index import Database


@dataclass
class Task:
    task_id: int
    task: str
    is_done: bool
    date: str


class TaskDB:
    def __init__(self, db_name: str):
        self.db = Database(db_name)

    def add_task(self, task: str, is_done: bool):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute('INSERT INTO tasks (task, is_done, date) VALUES (?, ?, ?)', task, int(is_done), date)

    def get_all_tasks(self) -> List[Task]:
        cursor = self.db.execute('SELECT * FROM tasks')
        return [Task(*row) for row in cursor.fetchall()]

    def get_task_by_id(self, task_id: int) -> Task:
        cursor = self.db.execute('SELECT * FROM tasks WHERE task_id = ?', task_id)
        task = cursor.fetchone()
        return Task(*task) if task else None

    def update_task(self, task_id: int, task: str, is_done: bool):
        self.db.execute('''
            UPDATE tasks 
            SET task = ?, is_done = ?
            WHERE task_id = ?
        ''', task, int(is_done), task_id)

    def delete_task(self, task_id: int):
        self.db.execute('DELETE FROM tasks WHERE task_id = ?', task_id)
