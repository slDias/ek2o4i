# -*- encoding: utf-8 -*-


class User(object):

    def __init__(self, ttask):
        """
        Represents a user that needs to run a task
        :param int ttask: ticks needed to end the task
        """
        self.task_tick_count = ttask

    def tick_task(self):
        """Removes a tick from the remaining tick count"""
        self.task_tick_count -= 1

    @property
    def task_ended(self):
        """
        True if the user's task has finished executing
        :rtype: bool
        """
        return self.task_tick_count <= 0
