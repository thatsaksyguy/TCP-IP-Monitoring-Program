import json
import socket

class TaskDistributor:
    def __init__(self, service_registry, config_manager):
        self.service_registry = service_registry
        self.config_manager = config_manager
    def distribute_tasks(self):
        if not self.config_manager.configs:
            print("No configuration loaded.")
            return
        for server, config in self.service_registry.services.items():
            try:
                # Establish TCP connection
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    # Extracting server and port from registered service
                    server_ip, server_port = server.split(':')
                    sock.connect((server_ip, int(server_port)))
                    print(f"Connected to {server}")
                    # Serialize config to JSON and send
                    message = json.dumps(config).encode('utf-8')
                    sock.sendall(message)

                    # Await for an acknowledgment
                    response = sock.recv(1024).decode('utf-8')
                    print(f"Received acknowledgment from {server}: {response}")

            except Exception as e:
                print(f"Error distributing tasks to {server}: {e}")