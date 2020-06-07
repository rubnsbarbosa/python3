'''
Given an array of integers, return indices of the two numbers such that theyadd up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# 1. brute force - complexity O(n^2)
n = [2, 7, 11, 15]
t = 9

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

#result = two_sum(n, t)
#print(result)

'''
Use some sort of data structure to temporarily store each elements as we go by in the array and if we subtract the target minus the actual element
and we just look for the complement of the number as we're traversing through the array. Bellow we have an example of complement
2 + 7 = 9 => 9 - 2 = 7 or 9 - 7 = 2
n = [2, 7, 11, 15]
We add the actual element in a HashMap and then we look if the complement is in the HashMap. So, in the first time we put 2 inside the HashMap, then
in the second time we check if 9 - 7 = 2 belong to the HashMap and return the indices.
'''

# 2. HashMap - complexity O(n)

def twoSum(nums, target):
    numMap = {}
    for i in range(0, len(nums)):
        if target - nums[i] in numMap:
            return [numMap[target - nums[i]] , i] # Complement found! Return the indices
        else:
            numMap[nums[i]] = i # Put the value with its index in the map

r = twoSum(n, t)
print(r)
