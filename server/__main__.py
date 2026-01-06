from .config import DevelopmentConfiguration
from .fms_server import FmsServer
from typing import cast


def main():

    server = FmsServer(DevelopmentConfiguration())
    server.logger.info("Main: FMS Server created")      
    server.run(host=cast(str, server.config["HOST"]), 
              port=cast(int,server.config["PORT"]), 
              debug=cast(bool, server.config["DEBUG"]))

    
if __name__ == "__main__":
    main()