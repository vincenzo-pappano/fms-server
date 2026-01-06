import os

class BaseConfiguration:

    DEV_REG_BASE_URL: str = "https://ext-api.device-registry.i2p2.iotecha.com"
    DEV_REG_API_VERSION: str = "v1"

    AWS_USERNAME: str | None = os.environ.get("AWS_USERNAME", "MISSING_USERNAME")
    AWS_PASSWORD: str | None = os.environ.get("AWS_PASSWORD", "MISSING_USERNAME")
    AWS_DURATION: int = 43200
    AWS_FLASHING_LIMIT: int = 8
    AWS_REGION: str = "us-east-1"
    AWS_SERVICE: str = "execute-api"

class DevelopmentConfiguration(BaseConfiguration):
    """Development configuration for the FMS Server."""

    HOST: str = "0.0.0.0"
    PORT: int = 5050
    DEBUG: bool = True


class ProductionConfiguration(BaseConfiguration):
    """Production configuration for the FMS Server."""

    FLASK_ENV: str = "production"
