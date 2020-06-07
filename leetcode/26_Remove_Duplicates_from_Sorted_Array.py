'''
We can do this using HashMap in order to store the elements. We go through the array and if an element already belongs to HashMap than we remove

Input
[1,1,2]
Output
[1,1]
Expected
[1,2]
'''

#n = [0,0,1,1,1,2,2,3,3,4]
n = [1,1,2]


def removeDuplicates(nums):
    numHashMap = {}
    for i in range(len(nums)):
        if nums[i] in numHashMap:
            pass
        else:
            numHashMap[nums[i]] = i

    return len(numHashMap)

def remove_duplicates(nums):
    if not nums:
        return 0

    count = 0
    for i in range(len(nums)):
        if nums[count] != nums[i]:
            count += 1
            nums[count] = nums[i]

    return count + 1

#print(remove_duplicates(n))


len = remove_duplicates(n)
for i in range(len):
    print(i)
