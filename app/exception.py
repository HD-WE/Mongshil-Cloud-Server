from flask.json import detect_encoding
from werkzeug.exceptions import HTTPException, default_exceptions

class MungshilException(HTTPException):
    pass

class WrongResource(MungshilException):
    code = 400
    description = "resource is wrong"

class SuccessRequest(MungshilException):
    code = 200
    description = "success return response"

class NotAllowedMethod(MungshilException):
    code = 405
    description = "not allowed method" 

class Unauthorized(MungshilException):
    code = 401
    default_exceptions = "unauthorized user"