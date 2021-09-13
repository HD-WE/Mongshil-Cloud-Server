from flask.json import detect_encoding
from werkzeug.exceptions import HTTPException

class MungshilException(HTTPException):
    pass

class WrongResource(MungshilException):
    code = 400
    description = "resource is wrong"

class SuccessRequest(MungshilException):
    code = 200
    description = "success return response"

class Unauthorized(MungshilException):
    code = 401
    default_exceptions = "unauthorized user"