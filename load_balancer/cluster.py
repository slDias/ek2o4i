# -*- encoding: utf-8 -*-

from operator import attrgetter


class Cluster(object):

    def __init__(self):
        self.server_list = []
        self.running_cost = 0

    def add_server(self, server):
        self.server_list.append(server)

    @property
    def has_server(self):
        return len(self.server_list) > 0

    def remove_unused_server(self):  # todo avoid iterating twice using for in range
        remove_index_list = []
        for server_index, server in enumerate(self.server_list):
            server.remove_finished_user()
            if server.has_any_user:
                continue
            remove_index_list.append(server_index)

        self.server_list = [server for index, server in enumerate(self.server_list) if index not in remove_index_list]

    def get_least_busy_server(self):
        """Returns the server with less users or any server that has room for a new user"""

        if not self.server_list:
            return None

        least_busy = min(self.server_list, key=attrgetter('user_count'))

        if least_busy.is_full:
            return None

        return least_busy

    def execute_server_task(self):
        for server in self.server_list:
            self.running_cost += 1
            server.run_user_task()

    def report(self):
        return ",".join([str(len(server.user_list)) for server in self.server_list]) or '0'
