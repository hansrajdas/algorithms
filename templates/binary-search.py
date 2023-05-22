def binarySearchFirstIdx(nums, x):
    """
    Returns first index of x in nums, see below examples for see behaviour
    with edge cases:
        assert binarySearchFirstIdx([5,10,15,20], 3) == 0
        assert binarySearchFirstIdx([5,10,15,20], 5) == 0
        assert binarySearchFirstIdx([5,10,15,20], 6) == 1  # 6 is not present
        assert binarySearchFirstIdx([5,10,15,20], 10) == 1
        assert binarySearchFirstIdx([5,10,15,20], 15) == 2
        assert binarySearchFirstIdx([5,10,15,20], 20) == 3
        assert binarySearchFirstIdx([5,10,15,20], 25) == 4
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    print("Left: %d" % left)
    return left

def binarySearch(nums, x):
    """
    Return index of x (any index if has duplicates), -1 otherwise.
    """
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

assert binarySearchFirstIdx([1,1,1,1,1,1,2,2,2,3,4,5,6,6,6,6,6,6,6], 0) == 0
assert binarySearchFirstIdx([1,1,1,1,1,1,2,2,2,3,4,5,6,6,6,6,6,6,6], 1) == 0
assert binarySearchFirstIdx([1,1,1,1,1,1,2,2,2,3,4,5,6,6,6,6,6,6,6], 2) == 6
assert binarySearchFirstIdx([1,1,1,1,1,1,2,2,2,3,4,5,6,6,6,6,6,6,6], 3) == 9
assert binarySearchFirstIdx([1,1,1,1,1,1,2,2,2,3,4,5,6,6,6,6,6,6,6], 4) == 10
assert binarySearchFirstIdx([1,1,1,1,1,1,2,2,2,3,4,5,6,6,6,6,6,6,6], 5) == 11
assert binarySearchFirstIdx([1,1,1,1,1,1,2,2,2,3,4,5,6,6,6,6,6,6,6], 6) == 12
assert binarySearchFirstIdx([1,1,1,1,1,1,2,2,2,3,4,5,6,6,6,6,6,6,6], 7) == 19
assert binarySearchFirstIdx([1], 0) == 0
assert binarySearchFirstIdx([1], 1) == 0
assert binarySearchFirstIdx([1], 2) == 1
assert binarySearchFirstIdx([5,10,15,20], 3) == 0
assert binarySearchFirstIdx([5,10,15,20], 5) == 0
assert binarySearchFirstIdx([5,10,15,20], 6) == 1  # 6 is not present
assert binarySearchFirstIdx([5,10,15,20], 10) == 1
assert binarySearchFirstIdx([5,10,15,20], 15) == 2
assert binarySearchFirstIdx([5,10,15,20], 20) == 3
assert binarySearchFirstIdx([5,10,15,20], 25) == 4
