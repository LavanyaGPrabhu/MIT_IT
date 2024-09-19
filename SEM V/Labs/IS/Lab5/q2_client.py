import socket

def compute_hash(data: str) -> str:
    # Compute the hash of the data using the DJB2 hash function
    hash_value = 5381
    for char in data:
        hash_value = (hash_value * 33) ^ ord(char)
    hash_value &= 0xFFFFFFFF
    return f"{hash_value}"  # Return hash in hexadecimal format

def client_program():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the local machine name
    host = socket.gethostname()
    port = 8888  # The same port as the server
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Data to be sent
    data = "hello"
    print(f"Sending data: {data}")
    
    # Send data to the server
    client_socket.send(data.encode())
    
    # Receive the hash from the server
    received_hash = client_socket.recv(1024).decode()
    print(f"Received hash from server: {received_hash}")
    
    # Compute the hash of the sent data
    computed_hash = compute_hash(data)
    print(f"Computed hash of the data: {computed_hash}")
    
    # Verify if the hashes match
    if received_hash == computed_hash:
        print("Data integrity verified: Hashes match.")
    else:
        print("Data integrity compromised: Hashes do not match.")
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    client_program()