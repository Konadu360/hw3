"""Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
"""
Given_nums = [1,1,2,2,2,3]

def rmduplicate1(nums):
#initialize a count
    index=0

    #loop through array and for each count compare items
    #if equal delete duplicate

    while index < len(nums)-1:
        if nums[index]==nums[index+1]:
            del nums[index+1]
            print(index,nums)
            continue
        index+=1
    return len(nums),nums

print(rmduplicate1(Given_nums))
