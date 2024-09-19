import socket
import hashlib

def compute_hash(data: str) -> str:
    # Compute the hash of the data using the DJB2 hash function
    hash_value = 5381
    for char in data:
        hash_value = (hash_value * 33) ^ ord(char)
    hash_value &= 0xFFFFFFFF
    return f"{hash_value}"  # Return hash in hexadecimal format

def server_program():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the local machine name
    host = socket.gethostname()
    port = 8888  # Reserve a port for the service
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Enable the server to accept connections (1 connection at a time)
    server_socket.listen(1)
    
    print(f"Server listening on {host}:{port}...")
    
    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")
    
    # Receive data from the client
    data = conn.recv(1024).decode()
    print(f"Received data: {data}")
    
    # Compute hash of the received data
    data_hash = compute_hash(data)
    
    # Send the hash back to the client
    conn.send(data_hash.encode())
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    server_program()

