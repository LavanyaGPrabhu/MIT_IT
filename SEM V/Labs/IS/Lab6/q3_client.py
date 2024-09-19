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

# Verifying the signature
def diffie_hellman_verify(p, g, public_key, message, r, s):
    hashed_message = int(sha256(message.encode()).hexdigest(), 16)
    left_side = (mod_exp(public_key, r, p) * mod_exp(r, s, p)) % p
    right_side = mod_exp(g, hashed_message, p)
    return left_side == right_side

# Client
def client_program():
    # Client configuration
    p = 23  # Small prime (use large primes for real-world scenarios)
    g = 5   # Primitive root

    # Key generation for the client
    client_public_key, client_private_key = diffie_hellman_keygen(p, g)

    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5001))  # Connect to server on port 5001

    # Exchange public keys with server
    client_socket.send(str(client_public_key).encode())
    server_public_key = int(client_socket.recv(1024).decode())
    print(f"Server Public Key: {server_public_key}")
    print(f"Client Public Key: {client_public_key}")

    # Receive signature (r, s) from server
    signature = client_socket.recv(1024).decode().split(',')
    r, s = int(signature[0]), int(signature[1])
    print(f"Received signature (r, s): {r}, {s}")

    # Verify the message
    message = "This is a secure message."
    is_valid = diffie_hellman_verify(p, g, server_public_key, message, r, s)
    print(f"Signature valid: {is_valid}")

    client_socket.close()

if __name__ == '__main__':
    client_program()
