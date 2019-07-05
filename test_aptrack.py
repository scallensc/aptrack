"""
Test functions from aptrack
"""

from unittest import mock
from aptrack import in_track

def test_in_track():
    ''' test in_track function returns expected output '''
    mock.builtins.input = lambda _: "test1234"
    assert in_track() == ("TEST1234", None)
