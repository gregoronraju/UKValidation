"""
# File          : validation.py
# Created       : 06/09/22 11:49 am
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
import re
from exceptions.postcode_exception import UKPCException

NON_ALPHA_RE = re.compile('[^A-Z0-9]+')
POSTCODE_RE = re.compile('^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA)'
                         ' ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]'
                         '{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$')


def validate_postcode(postcode):
    """Return a normalised postcode if valid else throws an exception"""

    postcode = NON_ALPHA_RE.sub('', postcode.upper())
    postcode = postcode[:-3] + ' ' + postcode[-3:]
    if POSTCODE_RE.match(postcode):
        return postcode
    raise UKPCException("Please check the format")
