def has_negatives(a):
    number_dictionary = {}
    result = [] #init a list to hold the result
    for num in a:   # Iterate through the list
        number_dictionary[num] = None
    for num in a: # iterate through the list, if the number is positive
        if num > 0:
            if num * -1 in number_dictionary: # If the number has a negative term in the dictioanry
                result.append(num) # Then add to the result list
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
