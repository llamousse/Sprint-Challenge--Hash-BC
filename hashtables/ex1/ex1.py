#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # enumerate() - adds counter to an iterable
    # used directly in for loops or converted into a list of
    # tuples

    # store info in hash table first
    # for key, weight in enumerate(weights):
    #     hash_table_insert(ht, weight, key)

    # if no 2 weights to compare
    if len(weights) < 2:
        return None

    # store each weight in input list as keys in hash table
    # key: weight / value: index
    for (i, w) in enumerate(weights):
        if i <= limit:
            hash_table_insert(ht, w, i)

    # If we store each weight's list index as its value, we can then check to see if 
    # the hash table contains an entry for `limit - weight`. 
    # If it does, then we've found the two items whose weights sum up to the `limit`!
    # check if difference from limit exists in hash table
    for (x, y) in enumerate(weights):
        w2 = limit - y
        i2 = hash_table_retrieve(ht, w2)
        
        if i2 is not None:
            if x > i2:
                return (x, i2) 
            else:
                return (i2, x)
    
    # if no matching pair found, return none
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")