from flask import request, current_app
from flask.typing import ResponseReturnValue
from server.extensions import dram


class AuthorizeHandler:
    
    def authorize(self) -> ResponseReturnValue:
        if request.method == "POST":
            return self.dram_authorize()
        return self.dram_verify_authorization()
    
    def dram_authorize(self) -> ResponseReturnValue:
        payload = request.get_json()
        payload['duration'] = current_app.config['AWS_DURATION'] 
        payload['flashing_sessions_limit'] = current_app.config['AWS_FLASHING_LIMIT'] 
        current_app.logger.info(payload)
        
        response = dram.authorize_device_registry(payload)
        current_app.logger.info(response)
        return {"info":"authorization successfull"}, 200
    
    def dram_verify_authorization(self) -> ResponseReturnValue:
        if dram.keys_valid:
            return {"status": "authorized"}, 200
        else:
            return {"status": "not authorized"}, 200
