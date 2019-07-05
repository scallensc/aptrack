"""
Test functions from aptrack
"""

from unittest import mock
from aptrack import in_track
from aptrack import show_tracking

def test_in_track():
    ''' test in_track function returns expected output '''
    mock.builtins.input = lambda _: "test1234"
    assert in_track() == ("TEST1234", None)

def test_show_tracking_1():
    ''' test show_tracking function with valid tracking number '''
    track_num = '6XXX12345678'
    error_response, track_response = show_tracking(track_num)
    assert error_response == None

def test_show_tracking_2():
    ''' test show_tracking function with invalid tracking number '''
    track_num = 'notarealnumber'
    error_response, track_response = show_tracking(track_num)
    assert error_response != None
