from flask import request, current_app
from flask.typing import ResponseReturnValue
from server.extensions import dram
from typing import Final

REQUIRED_LOGIN_PARAMETERS: Final = ("username", "password", "mfa_code")

class AuthorizeHandler:
    
    def authorize(self) -> ResponseReturnValue:
        if request.method == "POST":
            return self.dram_authorize()
        return self.dram_verify_authorization()
    
    def dram_authorize(self) -> ResponseReturnValue:
        
        login_request = request.get_json()
        if any(login_parameter not in login_request.keys() for login_parameter in REQUIRED_LOGIN_PARAMETERS):
            return {
                "error": "Incomplete login request! Required parameters: "
                + f"{', '.join(login_parameter for login_parameter in REQUIRED_LOGIN_PARAMETERS)}"
            }, 400
        
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
