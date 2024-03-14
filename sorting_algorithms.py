def bubble_sort(nums_og: list) -> list:
    nums = nums_og[:]
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] < nums[j+1]: continue
            a = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = a
    return nums

def insertion_sort(nums_og: list) -> list:
    nums = nums_og[:]
    for i in range(len(nums)):
        for j in range(i-1):
            if nums[j] < nums[i]: continue
            a = nums[i]
            nums[i] = nums[j]
            nums[j] = a
    return nums

def selection_sort(nums_og: list) -> list:
    nums = nums_og[:]
    for i in range(len(nums)-1):
        smallest = i
        for j in range(i, len(nums)):
            if nums[j] < nums[smallest]: smallest = j
        a = nums[smallest]
        nums[smallest] = nums[i]
        nums[i] = a
        print(nums)
    return nums

def merge_sort(nums_og: list) -> list:
    nums = nums_og[:]
    if len(nums) == 2:
        if nums[0] < nums[1]: return nums
        a = nums[0]
        nums[0] = nums[1]
        nums[1] = a
        return nums
    if len(nums) == 1: return nums
    mid = len(nums)//2
    x = merge_sort(nums[:mid])
    y = merge_sort(nums[mid:])

    for i in range(len(x)):
        if x[i] < y[i]:
            nums[2*i] = x[i]
            nums[2*i+1] = y[i]
    return merge_sort(x+y)

nums = [3, 5, 7, 2, 3, 1, 5, 7, 9, 4, 5, 8, 6, 11, 4, 0]

print(merge_sort(nums))