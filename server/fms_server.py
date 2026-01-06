from flask import Flask, make_response, Response
from server.config import BaseConfiguration, DevelopmentConfiguration
from server.handlers.health_handler import HealthHandler
from server.handlers.authorize_handler import AuthorizeHandler
from server.extensions import dram
from typing import Callable, Any


class EndPointAction:

    def __init__(self, action: Callable[..., Any]) -> None:
        self.action = action

    def __call__(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Response:
        return make_response(self.action(*args, **kwargs))



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
        self.add_endpoint('/health',    self.health_handler.health,       ["GET"])
        self.add_endpoint('/authorize', self.authorize_handler.authorize, ["GET","POST"])


    def add_endpoint(self, rule: str, handler: Callable[..., Any], methods: list[str]) -> None:
        # Parameters for app.add_url_rule(): 
        #    rule: A string representing the URL rule (e.g., '/', '/user/<username>').
        #    endpoint: The name for the route, used for URL generation with the url_for() function. If not provided, it defaults to the name of the view_func.
        #    view_func: The actual Python function to be called when a request matches the URL rule 
        self.add_url_rule(rule=rule, endpoint=rule.removeprefix('/'), view_func=EndPointAction(handler), methods=methods)