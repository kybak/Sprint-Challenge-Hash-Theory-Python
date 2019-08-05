#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)
    indices = None

    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    for i in range(len(weights)):
        weight = weights[i]
        diff = limit - weight
        n = hash_table_retrieve(ht, diff)
        if n is not None:
            indices = [i, n]
            indices.sort(reverse=True)
            break

    return indices


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
