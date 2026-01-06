from flask import Flask
from server.config import BaseConfiguration, DevelopmentConfiguration
from server.handlers.health_handler import HealthHandler
from server.handlers.authorize_handler import AuthorizeHandler
from server.extensions import dram

class FmsServer(Flask):

    def __init__(self, config: BaseConfiguration = DevelopmentConfiguration()):
        super().__init__(__name__)
        self.config.from_object(config)
        self.logger.info("Fms Server: Config")
        
        self.health_handler = HealthHandler()
        self.authorize_handler = AuthorizeHandler()
        
        dram.init_app(self)
        
        self.register_routes()
        
    def register_routes(self):
        self.add_url_rule('/health', 'health', self.health_handler.health, methods=["GET"])
        self.add_url_rule('/authorize', 'authorize', self.authorize_handler.authorize, methods=["GET","POST"])
