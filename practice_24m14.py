#From an array of length 2n
#get sum of min(a, b) for all possible ways to group the array into pairs
#return largest sum

def possible_pairs(array, prev=[]):
    if len(array) < 3:
        return [array]
    array_copy = array[:]
    length = len(array)
    output = []
    for i in range(0, length-1):
        array = array_copy[:]
        x = array.pop(0)
        y = array.pop(i)
        output.append(prev + possible_pairs(array, [[x, y]]))
    return output


nums = [1, 2, 3, 4, 5, 6]
print(possible_pairs(nums))

#[[1, 2], [3, 4]]