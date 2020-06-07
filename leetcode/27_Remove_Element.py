'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.

Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
'''

n = [0,1,2,2,3,0,4,2]

def remove_element(nums, val):
    if not nums:
        return 0

    i = 0
    count = 0
    while i < len(nums):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
        i += 1

    return count

print(remove_element(n, 2))
