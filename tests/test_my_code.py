from unittest.mock import patch

from my_code import create_dir, do_things


# works but you are mocking it for *all* modules
@patch('os.makedirs')
def test_create_dir(mock_makedirs):

    create_dir('some_path')

    mock_makedirs.assert_called_with('some_path', exist_ok=False)


# works and you are mocking it for the system under test
@patch('my_code.os.makedirs')
def test_create_dir_mock_relative(mock_makedirs):

    create_dir('some_path')

    mock_makedirs.assert_called_with('some_path', exist_ok=False)


# this test will fail because it is not with respect to the system under test
@patch('pkg_a.module_a.things_will_be_done_here')
def test_do_things(mock_things_will_be_done_here):

    do_things('things')

    mock_things_will_be_done_here.assert_called_once_with('things')


# this test will pass
@patch('my_code.things_will_be_done_here')
def test_do_things_relative(mock_things_will_be_done_here):

    do_things('things')

    mock_things_will_be_done_here.assert_called_once_with('things')
