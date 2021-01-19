"""Given an array of integers nums and integer target, 
return the indices of the two numbers such that they add up to target.
"""

"""
solution:eg if target=9, list=[2,7,11,15], means loop to get 2+7=target, 2+11=target, 2+15=target, 7+11=target
7+15=target, 11+15=target. 
this also means target - any of de numbers shud = one of de numbers in our list
eg target(9)-2=7 and we can return the index of 7 and 2
this can be done by keeping track of de returned number after subtraction using dict
"""
numb = [2,15,11,7,8,1]
targ = 9
#define function to execute code
def nums(data,target):
    #initialize an empty dict to track indexes
    dicta={}
    items=[]
    #loop through the given list and find the difference between the target and each value in list
    for indexes in range(0,len(data)):
        number=target-data[indexes]
    #check if the difference value exist in dict, return its index and current index of the iteration
    #if it doesn't exist, store it with its index as the value
        if number in dicta:
            new_list=dicta[number],indexes
            items.append(new_list)
        else:
            dicta[data[indexes]]=indexes
    #return empty list if target not met
    return items
print(nums(numb,targ))

"""
for array question that maintains order
"""
#define function to execude the code
def arrays(nums,target):
    dita={}
    data=[]
    #loop through the array of integers 
    for indexes in range(0,len(nums)):
        val=target-nums[indexes]
        if val in dita:
            a=dita[val],indexes
            data.append(a)
        else:
            dita[nums[indexes]]=indexes
    return data
# print(arrays(numb,targ))
            
#             return nums[indexes], nums[val]
#         initialize a variable to store sum of the numbers
#         for each index, loop over the array and add the numbers
#         sum=0
#         for numbers in range(indexes,len(nums)):
#             print('number is:',numbers,indexes,nums[numbers])
        
#             sum=sum+nums[numbers]

#             print('the sum',sum)
#             #if the sum equals the target, return the indexes of the numbers
#             if sum==target:
#                 return(indexes,numbers)
print(arrays(numb,targ))

