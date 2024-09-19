def djb2_hash(s: str) -> int:
    # Initial hash value
    hash_value = 5381
    # print(ord('e'))
    # Iterate over each character in the input string
    for char in s:
        # Update hash value using bitwise operations to mix the bits
        hash_value = (hash_value * 33)
        # print(hash_value)
        hash_value^=ord(char)
        # print(hash_value)
    # Ensure the hash value is within the 32-bit range
    hash_value &= 0xFFFFFFFF
    
    return hash_value

# Example usage
input_string = "example"
print(f"Hash value for '{input_string}': {djb2_hash(input_string)}")
input_string = "hello"
print(f"Hash value for '{input_string}': {djb2_hash(input_string)}")
