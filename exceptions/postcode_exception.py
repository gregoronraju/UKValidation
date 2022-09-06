"""
# 
# File          : postcode_exception.py
# Created       : 06/09/22 12:43 pm
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""


class UKPCException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Post Code Not Valid, {0} '.format(self.message)
        else:
            return 'PostCode not valid! Please check the format'
