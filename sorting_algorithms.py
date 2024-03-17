def bubble_sort(nums_og: list) -> list:
    '''
    Bubble Sort ordenado de menor a mayor, garantías del primero al último
    '''
    nums = nums_og[:]
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] < nums[j+1]: continue
            a = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = a
    return nums

def bubble_sort_rev(nums_og: list) -> list:
    '''
    Bubble Sort ordenado de menor a mayor, garantías del último al primero 
    '''
    nums = nums_og[:]
    for i in range(len(nums)-1):
        for j in range(len(nums)-1, i, -1):
            if nums[j-1] < nums[j]: continue
            a = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = a
    return nums

def insertion_sort(nums_og: list) -> list:
    '''
    Insertion Sort ordenado de menor a mayor, garantías del primero al último
    '''
    nums = nums_og[:]
    for i in range(1, len(nums)):
        for j in range(i-1):
            if nums[j] < nums[i]: continue
            a = nums.pop(i)
            nums.insert(j, a)
            break
    return nums

def insertion_sort_rev(nums_og: list) -> list:
    '''
    Insertion Sort ordenado de menor a mayor, garantías del último al primero 
    '''
    nums = nums_og[:]
    for i in range(len(nums)-1, -1, -1):
        for j in range(len(nums)-1, i, -1):
            if nums[i] < nums[j]: continue
            a = nums.pop(i)
            nums.insert(j, a)
            break
    return nums

def selection_sort(nums_og: list) -> list:
    '''
    Selection Sort ordenado de menor a mayor, garantías del primero al último
    '''
    nums = nums_og[:]
    for i in range(len(nums)-1):
        smallest = i
        for j in range(i, len(nums)):
            if nums[j] < nums[smallest]: smallest = j
        a = nums[smallest]
        nums[smallest] = nums[i]
        nums[i] = a
    return nums

def selection_sort_rev(nums_og: list) -> list:
    '''
    Selection Sort ordenado de menor a mayor, garantías del último al primero 
    '''
    nums = nums_og[:]
    for i in range(len(nums)-1, 0, -1):
        biggest = i
        for j in range(i):
            if nums[j] > nums[biggest]: biggest = j
        a = nums[biggest]
        nums[biggest] = nums[i]
        nums[i] = a
    return nums

def merge_sort(nums_og: list) -> list:
    '''
    Merge Sort ordenado de menor a mayor
    '''
    def merge(x: list, y: list) -> list:
        '''
        Adjunta 2 listas ordenadas de menor a mayor de tal manera que la lista adjunta esté ordenada de menor a mayor.
        Retorna la lista adjuntada.
        '''
        nums = []
        j = 0
        i = 0
        while i < len(x) and j < len(y):
            if x[i] > y[j]: nums.append(y[j]); j+=1
            else: nums.append(x[i]); i+=1
        if i < len(x): nums+=x[i:]
        if j < len(y): nums+=y[j:]
        return nums

    if len(nums_og) < 2:
        return nums_og
    nums = nums_og[:]
    half_length = len(nums)//2
    x = merge_sort(nums[:half_length])
    y = merge_sort(nums[half_length:])
    nums = merge(x, y)
    return nums

def merge_sort_inverted(nums_og: list) -> list:
    '''
    Merge Sort ordenado de mayor a menor
    '''
    def merge(x: list, y: list) -> list:
        '''
        Adjunta 2 listas ordenadas de mayor a menor de tal manera que la lista adjunta esté ordenada de mayor a menor.
        Retorna la lista adjuntada.
        '''
        nums = []
        j = 0
        i = 0
        while i < len(x) and j < len(y):
            if x[i] < y[j]: nums.append(y[j]); j+=1
            else: nums.append(x[i]); i+=1
        if i < len(x): nums+=x[i:]
        if j < len(y): nums+=y[j:]
        return nums

    if len(nums_og) < 2:
        return nums_og
    nums = nums_og[:]
    half_length = len(nums)//2
    x = merge_sort_inverted(nums[:half_length])
    y = merge_sort_inverted(nums[half_length:])
    nums = merge(x, y)
    return nums

#Array a ordenar
nums = [3, 5, 7, 2, 3, 1, 5, 7, 9, 4, 5, 8, 6, 11, 4, 0]

#print(bubble_sort(nums))
#print(bubble_sort_rev(nums))
#print(insertion_sort(nums))
#print(insertion_sort_rev(nums))
#print(selection_sort(nums))
#print(selection_sort_rev(nums))
#print(merge_sort(nums))
print(merge_sort_inverted(nums))