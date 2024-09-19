# import random
# import hashlib
# import logging
# from Crypto.PublicKey import RSA
# import logging

# # Configure logging to both file and console
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# # File handler
# file_handler = logging.FileHandler('key_management.log')
# file_handler.setLevel(logging.INFO)

# # Console handler
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)

# # Formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# console_handler.setFormatter(formatter)

# # Add handlers to logger
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)

# # Configure logging
# logging.basicConfig(filename='key_management.log', level=logging.INFO)

# class RabinKeyManagement:
#     def __init__(self, key_size=1024):
#         self.key_size = key_size
#         self.hospitals = {}

#     # Rabin Key Generation (p and q must be prime, p ≡ 3 mod 4, q ≡ 3 mod 4)
#     def generate_rabin_key_pair(self):
#         def get_prime(modulus):
#             while True:
#                 prime = random.getrandbits(self.key_size // 2)
#                 if prime % 4 == 3 and self.is_prime(prime):
#                     return prime

#         p = get_prime(3)
#         q = get_prime(3)
#         n = p * q
#         return {'public_key': n, 'private_key': (p, q)}

#     # Check for prime (Miller-Rabin test)
#     def is_prime(self, n, k=5):  # Number of tests
#         if n <= 1:
#             return False
#         if n <= 3:
#             return True
#         if n % 2 == 0 or n % 3 == 0:
#             return False
#         i = 5
#         while i * i <= n:
#             if n % i == 0 or n % (i + 2) == 0:
#                 return False
#             i += 6
#         return True

#     # Key Distribution API
#     def distribute_key(self, hospital_id):
#         if hospital_id not in self.hospitals:
#             keys = self.generate_rabin_key_pair()
#             self.hospitals[hospital_id] = keys
#             logging.info(f'Keys generated and distributed for {hospital_id}')
#             return keys
#         return self.hospitals[hospital_id]

#     # Key Revocation API
#     def revoke_key(self, hospital_id):
#         if hospital_id in self.hospitals:
#             del self.hospitals[hospital_id]
#             logging.info(f'Keys revoked for {hospital_id}')
#             return True
#         return False

#     # Key Renewal API
#     def renew_key(self, hospital_id):
#         if hospital_id in self.hospitals:
#             keys = self.generate_rabin_key_pair()
#             self.hospitals[hospital_id] = keys
#             logging.info(f'Keys renewed for {hospital_id}')
#             return keys
#         return False

# # Example Usage
# kms = RabinKeyManagement()

# # Generate and distribute keys
# hospital_a = 'Hospital_A'
# kms.distribute_key(hospital_a)

# # Revoke keys
# kms.revoke_key(hospital_a)

# # Renew keys
# kms.renew_key(hospital_a)

import random
import logging

# Configure logging
logging.basicConfig(filename='key_management.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def miller_rabin_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write (n - 1) as 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    def is_composite(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        if is_composite(a):
            return False
    return True

class RabinKeyManagement:
    def __init__(self, key_size=1024):
        self.key_size = key_size
        self.hospitals = {}
        print(f"Initialized RabinKeyManagement with key size {self.key_size}")

    def generate_rabin_key_pair(self):
        print("Generating Rabin key pair...")
        def get_prime():
            while True:
                prime = random.getrandbits(self.key_size // 2)
                if prime % 4 == 3 and self.is_prime(prime):
                    print(f"Generated prime: {prime}")
                    return prime
        
        p = get_prime()
        q = get_prime()
        n = p * q
        print(f"Generated key pair: public_key={n}, private_key=({p}, {q})")
        return {'public_key': n, 'private_key': (p, q)}

    def is_prime(self, n, k=5):
        return miller_rabin_test(n, k)

    def distribute_key(self, hospital_id):
        print(f"Distributing key for {hospital_id}...")
        if hospital_id not in self.hospitals:
            keys = self.generate_rabin_key_pair()
            self.hospitals[hospital_id] = keys
            logger.info(f'Keys generated and distributed for {hospital_id}')
            print(f"Keys distributed for {hospital_id}: {keys}")
            return keys
        print(f"Keys already exist for {hospital_id}")
        return self.hospitals[hospital_id]

    def revoke_key(self, hospital_id):
        print(f"Revoking key for {hospital_id}...")
        if hospital_id in self.hospitals:
            del self.hospitals[hospital_id]
            logger.info(f'Keys revoked for {hospital_id}')
            print(f"Keys revoked for {hospital_id}")
            return True
        print(f"No keys found for {hospital_id}")
        return False

    def renew_key(self, hospital_id):
        print(f"Renewing key for {hospital_id}...")
        if hospital_id in self.hospitals:
            keys = self.generate_rabin_key_pair()
            self.hospitals[hospital_id] = keys
            logger.info(f'Keys renewed for {hospital_id}')
            print(f"Keys renewed for {hospital_id}: {keys}")
            return keys
        print(f"No existing keys to renew for {hospital_id}")
        return False

# Example Usage
kms = RabinKeyManagement()

# Generate and distribute keys
hospital_a = 'Hospital_A'
kms.distribute_key(hospital_a)

# Revoke keys
kms.revoke_key(hospital_a)

# Renew keys
kms.renew_key(hospital_a)
