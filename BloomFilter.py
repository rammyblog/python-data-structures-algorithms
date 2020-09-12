"""
    Bloom filters: Lightweight version of a hash table. Efficient insertions and lookup.
    More space efficient than hash table, but this comes at the cost of having "false positives"
    for entry lookup.

    When should I use a Bloom filter?
    * I want a DF that allows for fast lookups and insertions. I care about how much space the DS uses.
    I do not care ig the DS sometimes indicate an item is present when in fact it is not

    Components of a bloom filter
    * bit_vector = vectors of bits

"""

import pyhash

bit_vector = [0] * 20

# Non-cryptographic hash functions (Murmur and FNV)
fav = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

# Calculate the output of FNV nad Murmur hash functions for Pikachu and Charmader
    
