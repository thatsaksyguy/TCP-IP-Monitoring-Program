import socket

# This sets up the server to listen on IP address 127.0.0.1 and port 65432.
# Both the IP address and port are hardcoded. To listen on a different IP address or port, you can change these values:
def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Accepted connection from {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)  # Echo back received data

if __name__ == "__main__":
    start_server()