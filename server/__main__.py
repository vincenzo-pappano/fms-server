from .config import DevelopmentConfiguration
from .fms_server import FmsServer


def main():

    server = FmsServer(DevelopmentConfiguration())
    server.logger.info("Main: FMS Server created")    
    
if __name__ == "__main__":
    main()