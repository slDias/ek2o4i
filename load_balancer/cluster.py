# -*- encoding: utf-8 -*-

from operator import attrgetter
from server import Server


class Cluster(object):

    def __init__(self):
        """Represents a set of servers"""
        self.server_list = []
        self.running_cost = 0

    def add_server(self, server):
        """
        Adds a server to the cluster
        :param Server server: The server to be added
        """
        self.server_list.append(server)

    @property
    def has_server(self):
        """
        True if there's any server on the cluster
        :rtype: bool
        """
        return len(self.server_list) > 0

    def remove_unused_server(self):
        """Removes server that do not have any user"""
        for index in range(len(self.server_list) - 1, -1, -1):
            self.server_list[index].remove_finished_user()
            if not self.server_list[index].has_any_user:
                del self.server_list[index]

    def get_least_busy_server(self):
        """
        Returns the server with less users or any server that has room for a new user
        :rtype: Server | None 
        """""
        if not self.server_list:
            return None

        least_busy = min(self.server_list, key=attrgetter('user_count'))

        if least_busy.is_full:
            return None

        return least_busy

    def execute_server_task(self):
        """Runs user's tasks in each server"""
        for server in self.server_list:
            self.running_cost += 1
            server.run_user_task()

    def report(self):
        """
        Generates a string containing the amount of users on each server
        :rtype: str
        """
        return ",".join([str(len(server.user_list)) for server in self.server_list]) or '0'
