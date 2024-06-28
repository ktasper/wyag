"""
Test Config
"""

import io

import pytest


@pytest.fixture
def toml_file():
    """
    # Mock file content
    To be called with mock_open.return_value = toml_file
    """
    mock_file = io.BytesIO(
        b"""
    [tool.poetry]
    name = "wyag"
    version = "2.3.4"
    """
    )
    yield mock_file
