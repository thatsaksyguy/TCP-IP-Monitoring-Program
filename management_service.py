import json
import socket
import sys
import threading
import time


class ManagementService:
    def __init__(self):
        # The server is currently hardcoded to listen on 127.0.0.1 on port 65432
        # If you would like to listen on a different port, you can change this
        self.monitoring_services = {"127.0.0.1:65432": {"status": "disconnected", "messages": []}}
    
    def load_and_send_configuration(self, ip, port):
        config = {
            "id": f"{ip.replace('.', '')}{port}",
            "servers": [{"server": "example.com", "tcp": {"port": 80}, "services": ["tcp"], "interval": 10}],
            "ip": ip,
            "port": port
        }

        max_retries = 3  # Maximum number of retries
        retry_delay = 5  # Delay between retries in seconds

        for attempt in range(max_retries):
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((ip, port))
                print(f"[{time.strftime('%x %X')}] ID: {config['id']} Initializing connection for {ip}:{port}... Attempt {attempt + 1}")
                self.monitoring_services[f"{ip}:{port}"]["status"] = "connected"
                client_socket.send(json.dumps(config).encode('utf-8'))
                print(f"[{time.strftime('%x %X')}] ID: {config['id']} Sending configuration to {ip}:{port}...")
                response = client_socket.recv(1024).decode('utf-8')
                print(f"[{time.strftime('%x %X')}] ID: {config['id']} Configuration received confirmation: {response}")
                client_socket.close()
                return
            except Exception as e:
                print(f"[{time.strftime('%x %X')}] ID: {config['id']} Attempt {attempt + 1} failed for {ip}:{port}")
                time.sleep(retry_delay)  # Wait before retrying

        # After exhausting all retries
        self.monitoring_services[f"{ip}:{port}"]["status"] = "disconnected"
        print(f"[{time.strftime('%x %X')}] ID: {config['id']} Connection attempts failed after {max_retries} retries for {ip}:{port}")
    def manage_connections(self):
        while True:
            for service, details in self.monitoring_services.items():
                ip, port_str = service.split(":")
                port = int(port_str)
                if details["status"] == "disconnected":
                    threading.Thread(target=self.load_and_send_configuration, args=(ip, port)).start()
            time.sleep(5)  # Check every 5 seconds
if __name__ == "__main__":
    ms = ManagementService()
    threading.Thread(target=ms.manage_connections).start()