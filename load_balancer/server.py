# -*- encoding: utf-8 -*-

import exceptions


class Server(object):

    def __init__(self, umax):
        self.user_list = []
        self.umax = umax

    @property
    def user_count(self):
        return len(self.user_list)

    @property
    def is_full(self):
        return self.user_count == self.umax

    @property
    def has_any_user(self):
        return self.user_count > 0

    def add_user(self, new_user):
        if self.is_full:
            raise exceptions.ServerIsFull

        self.user_list.append(new_user)

    def run_user_task(self):
        for user in self.user_list:
            user.tick_task()

    def remove_finished_user(self):  # todo avoid iterating twice
        remove_index_list = []
        for user_index, user in enumerate(self.user_list):
            if user.task_ended:
                remove_index_list.append(user_index)

        self.user_list = [user for index, user in enumerate(self.user_list) if index not in remove_index_list]
