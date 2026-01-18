##Overview
This project implements an LRU (Least Recently Used) cache in Python from scratch, using a doubly linked list and a hash map to achieve O(1) operations.
An LRU cache keeps track of recently used items, and deletes the least recently used item when the cache is full.
##Features
- O(1) get and add operations
- Tracks cache hits and cache misses
- Handles capacity by evicting least recently used item
##Classes
Link
- Represents a node in the DLL
- Stores key, data, next and previous references
- Methods: getKey(), getData(), setData(), getNext(), setNext(), getPrevious(), setPrevious(), isFirst(), isLast()
DLL
- Double linked list implementation
- Methods for inserting at the front and deleting from the end
- Handles first and last pointers
LRUcache
- Main cache class
- Maintains a DLL for order, and a hash map (Python dictionary) for lookups
- Methods: get(key): returns value if key is in cache, moves node to front, counts hit/miss |  add(key,data): adds a new value, evicts least recently used if full
##Usage
Included is a demo script. To run: python3 LRUcache.py

Sample usage:
from LRUcache import LRUcache
cache= LRUcache(10)
cache.add("A",40)
cache.add("B",50)
cache.get("A")
cache.get("C")
print("Hit rate:", cache.hits/(cache.hits + cache.misses))
