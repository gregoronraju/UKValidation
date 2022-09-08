"""
# File          : test_api.py
# Created       : 08/09/22 10:19 am
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
import json

from api.validation_api import app


def test_uk_postcode_validation():
    """Test the api with different post codes"""
    response = app.test_client().get('/pc_validation?postcode=ascN 1ZZ')
    res = json.loads(response.data)
    assert res['Postcode'] == "ASCN 1ZZ"

    response = app.test_client().get('/pc_validation?postcode=22cN 1ZZ')
    res = json.loads(response.data)
    assert res['Error'] == "Post Code Not Valid, Please check the format "

