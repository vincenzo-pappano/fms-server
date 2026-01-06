from flask import request, current_app
from flask.typing import ResponseReturnValue

class AuthorizeHandler:
    
    def __init__(self):
        self.authenticated = True
    
    def authorize(self) -> ResponseReturnValue:
        if request.method == "POST":
            return self.dram_authenticate()
        return self.dram_verify_authentication()
    
    def dram_authenticate(self) -> ResponseReturnValue:
        payload = request.get_json()
        current_app.logger.info(payload)
        payload['duration'] = current_app.config['AWS_DURATION'] 
        payload['flashing_sessions_limit'] = current_app.config['AWS_FLASHING_LIMIT'] 
        current_app.logger.info(payload)
        return {"info":"authorization successfull"}, 200
    
    def dram_verify_authentication(self) -> ResponseReturnValue:
        if self.authenticated:
            return {"status": "authorized"},200
        else:
            return {"status": "not authorized"}, 200
