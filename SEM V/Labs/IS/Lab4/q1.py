from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime
import random
import logging
import time

# Setup logging
logging.basicConfig(filename='key_management.log', level=logging.INFO)

class KeyManagementSystem:
    def generate_rsa_keys(self):
        """Generate RSA key pair."""
        key = RSA.generate(2048)
        logging.info(f'{time.ctime()} - RSA keys generated.')
        return key, key.publickey()

    def encrypt_rsa(self, public_key, message):
        """Encrypt a message using RSA."""
        cipher = PKCS1_OAEP.new(public_key)
        return cipher.encrypt(message)

    def decrypt_rsa(self, private_key, ciphertext):
        """Decrypt a message using RSA."""
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(ciphertext)

class Subsystem:
    def __init__(self, name, kms):
        self.name = name
        self.kms = kms
        self.private_rsa_key, self.public_rsa_key = self.kms.generate_rsa_keys()
        self.dh_private_key = None
        self.shared_secret = None

    def generate_dh_keys(self, prime, base):
        """Generate Diffie-Hellman keys."""
        self.dh_private_key = random.randint(2, prime-2)
        dh_public_key = pow(base, self.dh_private_key, prime)
        return dh_public_key

    def compute_shared_secret(self, dh_public_key, prime):
        """Compute shared secret using received DH public key."""
        self.shared_secret = pow(dh_public_key, self.dh_private_key, prime)
        logging.info(f'{time.ctime()} - {self.name}: Shared secret computed.')

    def send_message(self, recipient, message):
        """Encrypt and send a message using the shared secret."""
        if isinstance(message, str):
            message = message.encode('utf-8')
        encrypted_message = self.kms.encrypt_rsa(recipient.public_rsa_key, message)
        logging.info(f'{self.name} sent an encrypted message to {recipient.name}')
        return encrypted_message

    def receive_message(self, encrypted_message):
        """Decrypt and receive a message using the shared secret."""
        decrypted_message = self.kms.decrypt_rsa(self.private_rsa_key, encrypted_message)
        logging.info(f'{self.name} received a message')
        print(f'{self.name} received message: {decrypted_message.decode()}')

def main():
    kms = KeyManagementSystem()

    # Define prime and base for Diffie-Hellman
    prime = getPrime(256)
    base = 2

    # Create subsystems
    finance_system = Subsystem("Finance System", kms)
    hr_system = Subsystem("HR System", kms)
    supply_chain_system = Subsystem("Supply Chain Management", kms)

    # Each subsystem generates its DH public key
    finance_dh_pub = finance_system.generate_dh_keys(prime, base)
    hr_dh_pub = hr_system.generate_dh_keys(prime, base)
    supply_chain_dh_pub = supply_chain_system.generate_dh_keys(prime, base)

    # Simulate RSA encrypted exchange of DH public keys
    encrypted_dh_pub_to_hr = finance_system.send_message(hr_system, str(finance_dh_pub))
    encrypted_dh_pub_to_supply = hr_system.send_message(supply_chain_system, str(hr_dh_pub))
    encrypted_dh_pub_to_finance = supply_chain_system.send_message(finance_system, str(supply_chain_dh_pub))

    # HR and Finance decrypt and compute shared secret
    decrypted_finance_dh_pub = int(hr_system.kms.decrypt_rsa(hr_system.private_rsa_key, encrypted_dh_pub_to_hr))
    decrypted_hr_dh_pub = int(supply_chain_system.kms.decrypt_rsa(supply_chain_system.private_rsa_key, encrypted_dh_pub_to_supply))
    decrypted_supply_chain_dh_pub = int(finance_system.kms.decrypt_rsa(finance_system.private_rsa_key, encrypted_dh_pub_to_finance))

    # Compute shared secrets
    finance_system.compute_shared_secret(decrypted_hr_dh_pub, prime)
    hr_system.compute_shared_secret(decrypted_supply_chain_dh_pub, prime)
    supply_chain_system.compute_shared_secret(decrypted_finance_dh_pub, prime)

    # Finance sends a secure message to HR
    message = "Financial Report 2024"
    encrypted_message = finance_system.send_message(hr_system, message)
    hr_system.receive_message(encrypted_message)

    # HR sends a message to Supply Chain
    encrypted_message_to_supply = hr_system.send_message(supply_chain_system, "Procurement Order")
    supply_chain_system.receive_message(encrypted_message_to_supply)

    # Supply Chain sends a message to Finance
    encrypted_message_to_finance = supply_chain_system.send_message(finance_system, "Supply Chain Update")
    finance_system.receive_message(encrypted_message_to_finance)

if __name__ == "__main__":
    main()
