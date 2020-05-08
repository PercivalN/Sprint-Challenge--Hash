def has_negatives(a):
    number_dictionary = {}
    result = []
    for num in a:
        number_dictionary[num] = None
    for num in a:
        if num > 0:
            if num * -1 in number_dictionary:
                result.append(num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
