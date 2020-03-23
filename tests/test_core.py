import unittest
from unittest.mock import patch, mock_open, call


class TestCore(unittest.TestCase):
    def test_exists(self):
        from load_balancer import core

    def test_read_input_file(self):
        from load_balancer import core

        mock_file_path = "test_file"
        with patch("builtins.open", mock_open(read_data="1\n2\n3")) as _mock_open:
            core.main(mock_file_path)
            assert call(mock_file_path) in _mock_open.call_args_list

    def test_create_output_file(self):
        from load_balancer import core

        mock_file_path = "test_file"
        with patch("builtins.open", mock_open(read_data="1\n2\n3")) as _mock_open:
            core.main(mock_file_path)
            assert call('output.txt', 'a') in _mock_open.call_args_list

    @patch('load_balancer.core.User')
    def test_create_n_user(self, mock_user):
        from load_balancer import core

        mock_file_path = "test_file"
        with patch("builtins.open", mock_open(read_data="1\n2\n3")) as _mock_open:
            core.main(mock_file_path)
            assert mock_user.call_args_list.count(call(1)) == 3


if __name__ == '__main__':
    unittest.main()
