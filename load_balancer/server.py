# -*- encoding: utf-8 -*-

import exceptions
from user import User


class Server(object):

    def __init__(self, umax):
        """
        Represents a server capable of host users
        :param int umax: Maximum amount of user this server can handle
        """
        self.user_list = []
        self.umax = umax

    @property
    def user_count(self):
        """
        The amount of users hosted on this server
        :rtype: int
        """
        return len(self.user_list)

    @property
    def is_full(self):
        """
        True if there's no room available for more users
        :rtype: bool
        """
        return self.user_count == self.umax

    @property
    def has_any_user(self):
        """
        True if at least one user is being hosted on this server
        :rtype: bool
        """
        return self.user_count > 0

    def add_user(self, new_user):
        """
        Adds a new user to be hosted by this server
        :param User new_user: The new user to be hosted
        :raise: ServerIsFull: When trying to add a user to a full server
        """
        if self.is_full:
            raise exceptions.ServerIsFull

        self.user_list.append(new_user)

    def run_user_task(self):
        """Run all hosted user's tasks"""
        for user in self.user_list:
            user.tick_task()

    def remove_finished_user(self):
        """Remove users with finished tasks"""
        for index in range(len(self.user_list) - 1, -1, -1):
            if self.user_list[index].task_ended:
                del self.user_list[index]
