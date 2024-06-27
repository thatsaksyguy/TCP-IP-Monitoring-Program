import json
import socket
import threading
import time

def handle_client_connection(client_socket):
    def perform_service_check(config):
        server = config['server']
        port = config['tcp']['port']
        timeout_seconds = 10  # Timeout after 10 seconds if unable to connect
        try:
            # Create a socket object with IPv4 addressing and TCP stream
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout_seconds)
                sock.connect((server, port))
                # If connection succeeds
                return {"status": True, "message": f"Port {port} on {server} is open.", "server": server, "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ')}
        except Exception as e:
            # If fails (e.g., connection timeout, refused, etc.)
            return {"status": False, "message": f"Failed to connect to Port {port} on {server}: {e}", "server": server, "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ')}
    pending_results = []
    def send_results(results):
        try:
            client_socket.send(json.dumps(results).encode('utf-8'))
            print(f"[{time.strftime('%x %X')}] Results sent.")
            return True
        except Exception as e:
            print(f"[{time.strftime('%x %X')}] Failed to send results: {e}")
            return False
    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            config = json.loads(message.decode('utf-8'))
            print(f"[{time.strftime('%x %X')}] Received configuration: {config}")
            results = []
            for service in config["servers"]:
                check_result = perform_service_check(service)
                print(f"[{time.strftime('%x %X')}] Service testing for {service['server']}...")
                print(f"TCP Status: {check_result}")
                results.append(check_result)
            if not send_results(results):
                pending_results.extend(results)
    except Exception as e:
        print(f"[{time.strftime('%x %X')}] Error: {e}")
    finally:
        if pending_results:
            print(f"[{time.strftime('%x %X')}] Attempting to send pending results...")
            send_results(pending_results)
        client_socket.close()
def start_monitoring_service(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(5)
    print(f"Server listening on localhost:{port}")
    try:
        while True:
            client_sock, address = server.accept()
            print(f"Accepted connection from {address}")
            client_handler = threading.Thread(
                target=handle_client_connection,
                args=(client_sock,)
            )
            client_handler.start()
    finally:
        server.close()
if __name__ == '__main__':
    # Currently monitoring on port 65432, you can change this to listen on a different port
    start_monitoring_service(65432)