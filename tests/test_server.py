import unittest
from unittest.mock import MagicMock


class TestServer(unittest.TestCase):
    def test_exists(self):
        from load_balancer.server import Server

    def test_add_user(self):
        from load_balancer.server import Server

        mock_user = MagicMock()
        test_server = Server(3)
        test_server.add_user(mock_user)
        assert test_server.user_list[0] == mock_user

    def test_user_count(self):
        from load_balancer.server import Server

        mock_user = MagicMock()
        test_server = Server(3)
        test_server.add_user(mock_user)
        assert test_server.user_count == 1

    def test_is_full_positive(self):
        from load_balancer.server import Server

        mock_user = MagicMock()
        test_server = Server(1)
        test_server.add_user(mock_user)
        assert test_server.is_full

    def test_is_full_negative(self):
        from load_balancer.server import Server

        test_server = Server(1)
        assert test_server.is_full is False

    def test_has_any_user_positive(self):
        from load_balancer.server import Server

        mock_user = MagicMock()
        test_server = Server(3)
        test_server.add_user(mock_user)
        assert test_server.has_any_user is True

    def test_has_any_user_negative(self):
        from load_balancer.server import Server

        test_server = Server(3)
        assert test_server.has_any_user is False

    def test_run_user_task(self):
        from load_balancer.server import Server

        user_mock = MagicMock()
        test_server = Server(3)
        test_server.add_user(user_mock)
        test_server.run_user_task()
        user_mock.tick_task.assert_called()

    def test_remove_finished_user(self):
        from load_balancer.server import Server

        user_mock = MagicMock()
        test_server = Server(3)
        test_server.add_user(user_mock)
        user_mock.task_ended = True
        test_server.remove_finished_user()
        assert not test_server.user_list


if __name__ == '__main__':
    unittest.main()
