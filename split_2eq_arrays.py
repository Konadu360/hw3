"""
Given an array of integers greater than zero, find if it is possible to split it in two subarrays 
(without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.
"""

Givennums =[1,2,2,0,1]
def subarray(nums):
    for i in range(0,len(nums)):
    # i=0
    # while i<len(nums):
        if sum(nums[:i+1])==sum(nums[i+1:]):
            return nums[:i+1],nums[i+1:]
        # i+=1
 
     
print(subarray(Givennums))

# #define function to execute code
# def twosubarray(data):
#     leftsum=0
#     for i in range(0,len(data)):
#         leftsum+=data[i]
#         rightsum=0
#         for j in range(i+1,len(data)):
#             rightsum+=data[j]
#         if leftsum==rightsum:
#             return data[:i+1],data[i+1:]
# print(twosubarray(Givennums))




integ = [2,7,11,15,4]

def splitarray(nums):
    #initialize a variable to store sum of one subarray
    lsum=0
    #loop through array and iterate over each index
    for index,number in enumerate(nums):
        #increment lsum by adding value of the index
        lsum+=number
        #initialize a variable to store sum of 2nd subarray
        rsum=0
        #for each index, increment rsum by adding all integers to the right 
        for indices in range(index+1,len(nums)):
            rsum+=nums[indices]
        #if the two sub-arrays arequal, return the subarrays
        if lsum==rsum:
            return nums[:index+1],nums[index+1:]
    return []

# print(splitarray(integ))
# print(splitarray(Givennums))


Given_nums = [0,0,1,1,1,2,2,3,3,4]

def sortedarray(nums):
    i=0
    while i < len(nums)-1:
        if nums[i]==nums[i+1]:
            del nums[i+1]
            continue
        i+=1
    return len(nums),nums

    # dicta={}
    # new_list=[]
    # for i in nums:

    #     if i in dicta:
    #         dicta[i]+=1
    #     else:
    #         dicta[i]=1
    #         new_list.append(i)
    # print(len(dicta.keys()))
    # nums=list(dicta)
    # print(nums)
    # return len(new_list)
    # sortedarray=[]
    # count=0
    # sorteddict={}
        
    # for i in nums:
    #     if i in sorteddict:
    #         # sorteddict[i]+=1
    #         nums.pop(i)
    #         print(i,nums)
    #     else:
    #         sorteddict[i]=1
    #         print(sorteddict)

    #         # sortedarray.append(i)
    # return len(nums),nums
        

print(sortedarray(Given_nums))