import hashlib
import random
import string
import matplotlib.pyplot as plt
from collections import Counter

class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.entries = entries
        self.buckets = buckets
        self.left_table = {i: [] for i in range(buckets)}
        self.right_table = {i: [] for i in range(buckets)}

    def _hash(self, key, table):
        if table == 'left':
            hash_object = hashlib.sha1(bytes(key, 'utf-8'))
        else:  # right table
            hash_object = hashlib.md5(bytes(key, 'utf-8'))
        hex_dig = hash_object.hexdigest()
        return int(hex_dig, 16) % self.buckets

    def insert(self, key, value):
        left_hash = self._hash(key, 'left')
        right_hash = self._hash(key, 'right')

        if len(self.left_table[left_hash]) <= len(self.right_table[right_hash]):
            self.left_table[left_hash].append((key, value))
        else:
            self.right_table[right_hash].append((key, value))
    
    # Q2
    def insert(self, key, value):
        left_hash = self._hash(key, 'left')
        right_hash = self._hash(key, 'right')

        if len(self.left_table[left_hash]) <= len(self.right_table[right_hash]):
            self.left_table[left_hash].append((key, value))
        else:
            self.right_table[right_hash].append((key, value))
            
    # Q3
    def lookup(self, key):
        left_hash = self._hash(key, 'left')
        right_hash = self._hash(key, 'right')

        for k, v in self.left_table[left_hash]:
            if k == key:
                return v

        for k, v in self.right_table[right_hash]:
            if k == key:
                return v

        return None  # key not found
    

def generate_random_string():
    length = random.randint(1, 10)
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

# Generate a list of 1,000,000 random strings
randomStrings = [generate_random_string() for _ in range(1000000)]


# Create a DLeftHashTable with 1000 entries and 1000 buckets
hashTable = DLeftHashTable(1000, 1000)

# Generate index values for the table using both hash functions
left_hash_indices = [hashTable._hash(key, 'left') for key in randomStrings[:1000]]
right_hash_indices = [hashTable._hash(key, 'right') for key in randomStrings[:1000]]

# Print the first 10 indices for both hash functions to verify
print("First 10 indices for the left hash function:", left_hash_indices[:10])
print("First 10 indices for the right hash function:", right_hash_indices[:10])

# Create a DLeftHashTable with 1000 entries and 1000 buckets
hashTable = DLeftHashTable(1000, 1000)

# Generate index values for the table using both hash functions
left_hash_indices = [hashTable._hash(key, 'left') for key in randomStrings[:1000]]
right_hash_indices = [hashTable._hash(key, 'right') for key in randomStrings[:1000]]

# Count the number of collisions for each index value
left_collisions = Counter(left_hash_indices)
right_collisions = Counter(right_hash_indices)

# Prepare data for the plot
left_x = list(left_collisions.keys())
left_y = list(left_collisions.values())
right_x = list(right_collisions.keys())
right_y = list(right_collisions.values())

# Create a new figure
plt.figure(figsize=(12, 6))

# Plot the number of collisions for the left hash function
plt.subplot(1, 2, 1)
plt.scatter(left_x, left_y, color='blue')
plt.title('Left Hash Function')
plt.xlabel('Index Value')
plt.ylabel('#Collisions')

# Plot the number of collisions for the right hash function
plt.subplot(1, 2, 2)
plt.scatter(right_x, right_y, color='red')
plt.title('Right Hash Function')
plt.xlabel('Index Value')
plt.ylabel('#Collisions')

# Show the plot
plt.tight_layout()
plt.show()

'''
Q4
The plots show that the hotspots are collisions 1 and 2. Most of the points above 4 collisions are randomized. 
Where collisions 3 and 4 have more index values but not as much as 1 and 2. This just means the functions aren't implementing the 
task as well, meaning there are better ways to implement a function.
'''