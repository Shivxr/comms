import socket

def netcat_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to {host}:{port}")
        print("Type messages, 'exit' to quit.")

        while True:
            msg = input("> ")
            if msg.lower() == 'exit':
                break

            s.sendall(msg.encode())
            # Try to receive a response (if any)
            try:
                data = s.recv(1024)
                if not data:
                    print("Connection closed by server.")
                    break
                print("Received:", data.decode())
            except socket.timeout:
                # No data received
                pass

if __name__ == "__main__":
    # Replace with your Ubuntu VM IP address
    HOST = '192.168.1.13'
    PORT = 12345
    netcat_client(HOST, PORT)
