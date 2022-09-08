"""
# File          : validation_api.py
# Created       : 07/09/22 8:10 pm
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
from flask import Flask, request, jsonify
from ukpcvalidationlib.validation import validate_postcode
from exceptions.postcode_exception import UKPCException

app = Flask(__name__)


@app.route('/pc_validation', methods=['GET'])
def uk_postcode_validation():
    """Return a normalised postcode if valid else returns a response with error message"""
    postcode = request.args.get('postcode')
    try:
        validate_code = validate_postcode(postcode)
        return jsonify({"Postcode": validate_code})
    except UKPCException as err:
        return jsonify({"Error": str(err)})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
