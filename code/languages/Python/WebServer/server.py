import socket

from loguru import logger


class WebServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None

        self.create_server()

    def create_server(self):
        """
        Create a basic server
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))

        logger.info(f"Server started on {self.host}:{self.port}")

        return self.server

    def __enter__(self):
        self.server.listen(5)

        return self.server

    def __exit__(self, exc_type, exc_value, traceback):
        self.server.close()

        logger.info("Server closed")


if __name__ == "__main__":
    HOST = ""
    PORT = 32271

    with WebServer(HOST, PORT) as server:
        pass
