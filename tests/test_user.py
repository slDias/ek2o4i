import unittest


class TestUser(unittest.TestCase):
    def test_exists(self):
        from load_balancer.user import User

    def test_task_tick_counter(self):
        from load_balancer.user import User

        test_user = User(5)
        test_user.tick_task()
        assert test_user.task_tick_count == 4

    def test_task_ended(self):
        from load_balancer.user import User

        test_user = User(1)
        test_user.tick_task()
        assert test_user.task_ended


if __name__ == '__main__':
    unittest.main()
