

def get_indices_of_item_weights(weights, length, limit):
    
    # Init a dictionary
    index_dictionay = {}
    
    for i in range(len(weights)):
        if weights[i] not in index_dictionay:
            index_dictionay[weights[i]] = [i]
        else:
            index_dictionay[weights[i]] += [i]
    
    # Iterate through the weights to see if they are over the limit      
    for weight in weights:
        if limit - weight in index_dictionay:
            if weight == limit - weight:
                return [index_dictionay[weight][1], index_dictionay[weight][0]]
            if weight > index_dictionay[limit - weight][0]:
                return [index_dictionay[limit - weight][0], index_dictionay[weight][0]]
            else:
                return [index_dictionay[weight][0], index_dictionay[limit - weight][0]]
            
    return None


