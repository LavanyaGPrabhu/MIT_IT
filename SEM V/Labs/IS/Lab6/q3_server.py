import socket
import random
from hashlib import sha256

# Function for modular exponentiation
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Diffie-Hellman key exchange
def diffie_hellman_keygen(p, g):
    private_key = random.randint(2, p - 2)
    public_key = mod_exp(g, private_key, p)
    return public_key, private_key

# Signing the message
def diffie_hellman_sign(p, g, private_key, message):
    hashed_message = int(sha256(message.encode()).hexdigest(), 16)
    k = random.randint(2, p - 2)
    r = mod_exp(g, k, p)
    k_inv = pow(k, -1, p - 1)  # Modular inverse of k mod (p-1)
    s = (hashed_message - private_key * r) * k_inv % (p - 1)
    return r, s

# Server
def server_program():
    # Server configuration
    p = 23  # Small prime (use large primes for real-world scenarios)
    g = 5   # Primitive root

    # Key generation for the server
    server_public_key, server_private_key = diffie_hellman_keygen(p, g)

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5001))  # Bind to localhost and port 5001
    server_socket.listen(1)

    print("Server listening on port 5001...")
    conn, address = server_socket.accept()
    print(f"Connection from: {address}")

    # Exchange public keys with client
    client_public_key = int(conn.recv(1024).decode())
    conn.send(str(server_public_key).encode())
    print(f"Client Public Key: {client_public_key}")
    print(f"Server Public Key: {server_public_key}")

    # Sign the message
    message = "This is a secure message."
    r, s = diffie_hellman_sign(p, g, server_private_key, message)
    conn.send(f"{r},{s}".encode())
    print(f"Sent signature (r, s): {r}, {s}")

    conn.close()

if __name__ == '__main__':
    server_program()
