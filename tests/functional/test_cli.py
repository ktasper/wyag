import os

import pytest


@pytest.mark.parametrize("test_input,expected_exit_code", [("version", 0), ("", 512)])
def test_entrypoint(test_input, expected_exit_code):
    exit_status = os.system(f"./wyag.py {test_input}")
    assert exit_status == expected_exit_code
