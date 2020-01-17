#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # hash 
    # key:starting location / value: destination
    # 'i'th location in route can be found by checking
    # the hash table for the 'i-1'th location

    # hash ticket with 
    # key(t.source) and value(t.destination)
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)
    
    # get first ticket since ticket source is "NONE"
    destination = hash_table_retrieve(hashtable, "NONE")
    i = 0
    while i < len(route):
        route[i] = destination
        i += 1
        destination = hash_table_retrieve(hashtable, destination)
    
    return route
