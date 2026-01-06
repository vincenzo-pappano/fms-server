from flask import Flask
from flask.typing import ResponseReturnValue
from .config import BaseConfiguration, DevelopmentConfiguration


def health() -> ResponseReturnValue:
    return {"info":"HEALTH Page"}, 200
    


class FmsServer(Flask):

    def __init__(self, config: BaseConfiguration = DevelopmentConfiguration()):
        super().__init__(__name__)
        self.config.from_object(config)
        self.logger.info("Fms Server: Config")
        
        self.register_routes()
        
    def register_routes(self):
        self.add_url_rule('/health', 'health', health, methods=["GET"])
