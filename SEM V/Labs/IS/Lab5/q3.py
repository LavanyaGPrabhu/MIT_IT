import time
import hashlib
import random
import string

# Function to generate a random string of a given length
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to compute hash values using a given hash function
def compute_hash(hash_func, data):
    hasher = hash_func()
    hasher.update(data.encode('utf-8'))
    return hasher.hexdigest()

# Function to analyze hash performance and collision resistance
def analyze_hash_performance(num_strings=50, min_length=8, max_length=16):
    # Generate random strings
    strings = [generate_random_string(random.randint(min_length, max_length)) for _ in range(num_strings)]
    
    # Initialize data structures for measuring time and detecting collisions
    hash_times = {'md5': 0, 'sha1': 0, 'sha256': 0}
    hash_values = {'md5': set(), 'sha1': set(), 'sha256': set()}
    collisions = {'md5': 0, 'sha1': 0, 'sha256': 0}

    # Measure hash computation time and detect collisions
    for s in strings:
        # MD5
        start_time = time.time()
        md5_hash = compute_hash(hashlib.md5, s)
        hash_times['md5'] += time.time() - start_time
        if md5_hash in hash_values['md5']:
            collisions['md5'] += 1
        hash_values['md5'].add(md5_hash)

        # SHA-1
        start_time = time.time()
        sha1_hash = compute_hash(hashlib.sha1, s)
        hash_times['sha1'] += time.time() - start_time
        if sha1_hash in hash_values['sha1']:
            collisions['sha1'] += 1
        hash_values['sha1'].add(sha1_hash)

        # SHA-256
        start_time = time.time()
        sha256_hash = compute_hash(hashlib.sha256, s)
        hash_times['sha256'] += time.time() - start_time
        if sha256_hash in hash_values['sha256']:
            collisions['sha256'] += 1
        hash_values['sha256'].add(sha256_hash)

    # Report results
    print("Hash Computation Times (seconds):")
    for algo, total_time in hash_times.items():
        print(f"{algo.upper()}: {total_time:.6f}")

    print("\nNumber of Collisions Detected:")
    for algo, count in collisions.items():
        print(f"{algo.upper()}: {count}")

# Example usage
if __name__ == "__main__":
    analyze_hash_performance()
