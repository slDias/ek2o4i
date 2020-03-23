# -*- encoding: utf-8 -*-


class User(object):

    def __init__(self, ttask):
        self.task_tick_count = ttask

    def tick_task(self):
        self.task_tick_count -= 1

    @property
    def task_ended(self):
        return self.task_tick_count == 0
