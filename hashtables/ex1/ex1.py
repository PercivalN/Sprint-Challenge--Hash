from hashtable import(HashTable, get, put)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for key, value in enumerate(weights):
        put(ht, value, key)

    for key, value in enumerate(weights):
        if get(ht, limit - value) is not None:
            index = get(ht, limit - value)

            if index >= key:
                return [index, key]
            else:
                return [key, index]

    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
