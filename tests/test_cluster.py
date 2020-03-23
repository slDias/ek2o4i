import unittest
from unittest.mock import MagicMock


class TestCluster(unittest.TestCase):
    def test_exists(self):
        from load_balancer.cluster import Cluster

    def test_add_server(self):
        from load_balancer.cluster import Cluster

        mock_server = MagicMock()
        test_cluster = Cluster()
        test_cluster.add_server(mock_server)
        assert test_cluster.server_list[0] == mock_server

    def test_has_server_positive(self):
        from load_balancer.cluster import Cluster

        mock_server = MagicMock()
        test_cluster = Cluster()
        test_cluster.add_server(mock_server)
        assert test_cluster.has_server

    def test_has_server_negative(self):
        from load_balancer.cluster import Cluster

        test_cluster = Cluster()
        assert not test_cluster.has_server

    def test_remove_unused_server(self):
        from load_balancer.cluster import Cluster

        mock_server = MagicMock()
        mock_server.has_any_user = False
        test_cluster = Cluster()
        test_cluster.add_server(mock_server)
        test_cluster.remove_unused_server()
        assert not test_cluster.server_list

    def test_get_least_busy_server(self):
        from load_balancer.cluster import Cluster

        mock_server_busy = MagicMock()
        mock_server_busy.user_count = 10
        mock_server_busy.is_full = False

        mock_server_free = MagicMock()
        mock_server_free.user_count = 0
        mock_server_free.is_full = False

        test_cluster = Cluster()
        test_cluster.add_server(mock_server_busy)
        test_cluster.add_server(mock_server_free)

        self.assertEqual(mock_server_free, test_cluster.get_least_busy_server())

    def test_execute_server_task(self):
        from load_balancer.cluster import Cluster

        mock_server = MagicMock()
        mock_server.has_any_user = False
        test_cluster = Cluster()
        test_cluster.add_server(mock_server)
        test_cluster.execute_server_task()
        mock_server.run_user_task.assert_called()

    def test_report(self):
        from load_balancer.cluster import Cluster

        test_server = MagicMock()
        test_server.user_list = [None]
        test_cluster = Cluster()
        test_cluster.add_server(test_server)
        self.assertEqual('1', test_cluster.report())


if __name__ == '__main__':
    unittest.main()
