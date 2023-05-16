def binary_search(nums, x):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
