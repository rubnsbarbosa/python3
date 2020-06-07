'''
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''

n = [1,3,5,6]
t = 5

n1 = [1,3,5,6]
t1= 2

n2 = [1,3,5,6]
t2 = 7

n3 = [1,3,5,6]
t3 = 0

n4 = [3,6,7,8,10]
t4 = 5

n5 = [2,3,4,7,8,9]
t5 = 11

def search_insert(nums, target):
    if target > nums[len(nums) - 1]:
        return len(nums)

    for i in range(len(nums)):
        if nums[i] >= target:
            return i



print(search_insert(n1, t1))
