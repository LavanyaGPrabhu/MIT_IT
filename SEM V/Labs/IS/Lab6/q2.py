import random
from hashlib import sha256

# Function to compute modular exponentiation
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Diffie-Hellman key exchange
def diffie_hellman_keygen(p, g):
    # Private key
    private_key = random.randint(2, p - 2)
    # Public key
    public_key = mod_exp(g, private_key, p)
    print(f"Generated private key: {private_key}")
    print(f"Generated public key: {public_key}")
    return public_key, private_key

# Signing the message
def diffie_hellman_sign(p, g, private_key, message):
    print(f"\nSigning message: {message}")
    hashed_message = int(sha256(message.encode()).hexdigest(), 16)
    print(f"Hashed message (H(m)): {hashed_message}")
    
    k = random.randint(2, p - 2)
    r = mod_exp(g, k, p)
    k_inv = pow(k, -1, p - 1)  # Modular inverse of k mod (p-1)
    
    print(f"Calculated r: {r}")
    print(f"Modular inverse of k: {k_inv}")
    
    s = (hashed_message - private_key * r) * k_inv % (p - 1)
    print(f"Calculated signature s: {s}")
    
    return r, s

# Verifying the signature
def diffie_hellman_verify(p, g, public_key, message, r, s):
    print(f"\nVerifying signature for message: {message}")
    hashed_message = int(sha256(message.encode()).hexdigest(), 16)
    print(f"Hashed message (H(m)): {hashed_message}")
    
    left_side = (mod_exp(public_key, r, p) * mod_exp(r, s, p)) % p
    right_side = mod_exp(g, hashed_message, p)
    
    print(f"Left side of verification equation: {left_side}")
    print(f"Right side of verification equation: {right_side}")
    
    return left_side == right_side

# Example usage:
p = 23  # A small prime for demonstration (use larger primes in practice)
g = 5   # A primitive root modulo 23

# Key generation for Alice
print("=== Diffie-Hellman Key Generation (Alice) ===")
alice_public_key, alice_private_key = diffie_hellman_keygen(p, g)

# Signing a message
message = "This is a test message."
print("\n=== Signing ===")
r, s = diffie_hellman_sign(p, g, alice_private_key, message)

# Verifying the signature
print("\n=== Verification ===")
is_valid = diffie_hellman_verify(p, g, alice_public_key, message, r, s)
print(f"\nDiffie-Hellman Signature valid: {is_valid}")
