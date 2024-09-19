# import random
# from hashlib import sha256
# import math

# # Helper function to check if two numbers are coprime
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def elgamal_keygen(p, g):
#     x = random.randint(2, p - 2)  # private key
#     y = pow(g, x, p)              # public key
#     return (p, g, y), x

# def elgamal_sign(p, g, x, message):
#     while True:
#         k = random.randint(2, p - 2)
#         # Ensure k is coprime with p-1
#         if gcd(k, p - 1) == 1:
#             break
#     r = pow(g, k, p)
#     H_m = int(sha256(message.encode()).hexdigest(), 16)
#     k_inv = pow(k, -1, p - 1)  # Find modular inverse of k modulo (p - 1)
#     s = (H_m - x * r) * k_inv % (p - 1)
#     return r, s

# def elgamal_verify(p, g, y, message, r, s):
#     H_m = int(sha256(message.encode()).hexdigest(), 16)
#     left_side = (pow(y, r, p) * pow(r, s, p)) % p
#     right_side = pow(g, H_m, p)
#     return left_side == right_side

# # Example usage:
# p = 23  # A small prime for demonstration (use larger primes in practice)
# g = 5   # A primitive root modulo 23

# # Key generation
# public_key, private_key = elgamal_keygen(p, g)

# # Signing a message
# message = "This is a test message."
# r, s = elgamal_sign(p, g, private_key, message)

# # Verifying the signature
# is_valid = elgamal_verify(p, g, public_key[2], message, r, s)
# print(f"ElGamal Signature valid: {is_valid}")

import random
from hashlib import sha256
import math

# Helper function to check if two numbers are coprime
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def elgamal_keygen(p, g):
    x = random.randint(2, p - 2)  # private key
    y = pow(g, x, p)              # public key
    print(f"Generated private key: {x}")
    print(f"Generated public key: {y}")
    return (p, g, y), x

def elgamal_sign(p, g, x, message):
    print(f"Signing message: {message}")
    while True:
        k = random.randint(2, p - 2)
        # Ensure k is coprime with p-1
        if gcd(k, p - 1) == 1:
            print(f"Found valid k: {k}")
            break
        else:
            print(f"Invalid k (not coprime with p-1): {k}, retrying...")
    
    r = pow(g, k, p)
    print(f"Calculated r: {r}")
    
    H_m = int(sha256(message.encode()).hexdigest(), 16)
    print(f"Hashed message (H(m)): {H_m}")
    
    k_inv = pow(k, -1, p - 1)  # Find modular inverse of k modulo (p - 1)
    print(f"Modular inverse of k: {k_inv}")
    
    s = (H_m - x * r) * k_inv % (p - 1)
    print(f"Calculated signature s: {s}")
    
    return r, s

def elgamal_verify(p, g, y, message, r, s):
    print(f"Verifying signature for message: {message}")
    
    H_m = int(sha256(message.encode()).hexdigest(), 16)
    print(f"Hashed message (H(m)): {H_m}")
    
    left_side = (pow(y, r, p) * pow(r, s, p)) % p
    right_side = pow(g, H_m, p)
    
    print(f"Left side of verification equation: {left_side}")
    print(f"Right side of verification equation: {right_side}")
    
    return left_side == right_side

# Example usage:
p = 23  # A small prime for demonstration (use larger primes in practice)
g = 5   # A primitive root modulo 23

# Key generation
print("=== Key Generation ===")
public_key, private_key = elgamal_keygen(p, g)

# Signing a message
message = "This is a test message."
print("\n=== Signing ===")
r, s = elgamal_sign(p, g, private_key, message)

# Verifying the signature
print("\n=== Verification ===")
is_valid = elgamal_verify(p, g, public_key[2], message, r, s)
print(f"\nElGamal Signature valid: {is_valid}")
