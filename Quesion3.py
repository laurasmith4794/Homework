# 3.1

# A hash function is a function that takes an object as input and returns an integer value as output.

# Define a large prime number
PRIME = 1000000007

# Define a basic hash function for strings
def basic_hash(string):
    # Initialize the hash value to zero
    hash_value = 0
    # Loop through each character in the string
    for char in string:
        # Add the ASCII value of the character to the hash value
        hash_value += ord(char)
        # Take the remainder of dividing by the prime number
        hash_value %= PRIME
    # Return the hash value
    return hash_value

# 3.2 No hash collision

print(basic_hash("Girl")) # 398
print(basic_hash("Code")) # 379

# Both strings have different hash values and indices in the hash table.
# There is no collision between the two outputs so they can be stored and retrieved without any conflict.

# 3.3 Hash collision

# A hash collision is when two different inputs produce the same hash value using a hash function.
# For example, with this basic hash function, the strings “ABC” and “CBA” will both have a hash value of 198.
# Hash collisions can cause problems in data structures that rely on the uniqueness of hash values, such as hash tables.
# A way to handle hash collisions is by chaining.

print(basic_hash("ABC")) # 198
print(basic_hash("CBA")) # 198