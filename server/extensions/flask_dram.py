

from typing import Optional, Union
from flask import Flask
from requests_auth_aws_sigv4 import AWSSigV4 # type: ignore
import requests
import time


class DeviceRegistryAccessModel:
    
    def __init__(self) -> None:
        self.init_done: bool = False
        self.key_expiration_time: float = 0
        self.flashing_sessions_remaining: int = 0
        self.aws_auth: Optional[AWSSigV4] = None
        self.app: Optional[Flask] = None
        
    def init_app(self, app: Flask) -> None:
        self.app = app
        self.base_url: str = app.config["DEV_REG_BASE_URL"]
        self.api_version: str = app.config["DEV_REG_API_VERSION"]        
        
    def authorize_device_registry(self, login_request: dict[str,Union[str,int]]) -> requests.Response:
        resp = requests.post(f"{self.base_url}/{self.api_version}/authorize", json=login_request)
        assert self.app is not None
        self.app.logger.info(f"Response Status Code: {resp.status_code}")
        return resp
    
    @property
    def keys_valid(self) -> bool:
        if not self.init_done:
            return False
        if not self.key_expiration_time > time.time():
            return False
        if not self.flashing_sessions_remaining > 1:
            return False
        return True    