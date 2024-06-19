from unittest.mock import patch
from libs.version import cmd_version, get_version
from argparse import Namespace
import io


@patch("libs.version.get_version")
def test_cmd_version(mock_get_version, capsys):
    """
    Tests the cmd_version function prints
    to stdout
    """
    mock_get_version.return_value = "1.0.0"
    args = Namespace()  # Empty namespace for arguments
    cmd_version(args)
    captured = capsys.readouterr()
    assert captured.out == "1.0.0\n"


@patch("builtins.open", autospec=True)  # Mock open function
def test_get_version(mock_open):
    """
    Tests the get_version function can read a toml
    file and returns the version as a string.
    """
    # Mock file content with expected data
    mock_file = io.BytesIO(b"""
    [tool.poetry]
    name = "wyag"
    version = "2.3.4"
    """)
    mock_open.return_value = mock_file
    args = Namespace()
    version = get_version(args)
    # Assert returned version matches mock data
    assert version == "2.3.4"
    # Verify open was called with correct arguments *including binary mode*
    mock_open.assert_called_once_with("./pyproject.toml", "rb")
