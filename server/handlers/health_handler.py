from flask.typing import ResponseReturnValue
class HealthHandler:
    
    def health(self) -> ResponseReturnValue:
        return {"info":"HEALTH Page"}, 200        