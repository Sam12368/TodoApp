class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = {"id": self.next_id, "title": title}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all(self):
        return self.tasks

    def delete_task(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                self.tasks.remove(t)
                return True
        return False
