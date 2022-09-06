"""
# 
# File          : test_validation.py
# Created       : 06/09/22 11:50 am
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
from ukpcvalidationlib.validation import validate_postcode
from exceptions.postcode_exception import UKPCException


def test_valid_postcode():
    """Test case for valid format"""
    assert validate_postcode("NG80 1LH") == "NG80 1LH"


def test_invalid_postcode():
    """Test case for checking invalid formats"""
    try:
        validate_postcode("hhjj 8808")
        assert False
    except UKPCException:
        assert True


def test_format_postcode():
    """Test Case to check if lower case is accepted or not"""
    assert validate_postcode('ph1 5RB') == "PH1 5RB"

