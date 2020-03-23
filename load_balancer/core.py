# -*- encoding: utf-8 -*-

import sys
from server import Server
from user import User
from cluster import Cluster


def main(input_file_path):

    # Read input file
    with open(input_file_path) as input_file:
        ttask, umax, *new_user_per_tick = [int(line) for line in input_file.read().splitlines()]

    tick = 0
    cluster = Cluster()
    while tick < len(new_user_per_tick) or cluster.has_server:

        # Add new users to servers
        if tick < len(new_user_per_tick):
            for _ in range(new_user_per_tick[tick]):

                new_user = User(ttask)

                least_busy_server = cluster.get_least_busy_server()

                # Create a new server if all servers are busy
                if not least_busy_server:
                    new_server = Server(umax)
                    new_server.add_user(new_user)
                    cluster.add_server(new_server)
                    continue

                least_busy_server.add_user(new_user)

            tick += 1

        # Executes tasks and removes unused servers
        print(cluster.report())
        cluster.execute_server_task()
        cluster.remove_unused_server()

    print(cluster.running_cost)


if __name__ == '__main__':
    main(sys.argv[1])
