

"""Given an array of integers nums and integer target, 
return the indices of the two numbers such that they add up to target.
"""
# numb = [2,15,11,7,8,1]
# targ = 9

# #initialize empty dict and list
# dicta={}
# new=[]

# # loop through list and subtract from target
# for i, j in enumerate(numb):
#     data=targ-j

#     #if results is in dictionary, store index of current iteration and index of 
#     # value in dictionary into new list. if not in dictionary,
#     # store value with its index as key and value 
#     if data in dicta:
#         newlist=dicta[data], i
#         print(newlist)
#     else:
#         dicta[j]=i



numb = [2,15,11,7,8,1]
targ = 9

#initialize empty dict 
dicta={}
new =[]

# loop through list and subtract from target

for i in range(len(numb)):
    data=targ-numb[i]

    #if results is in dictionary, store index of current iteration and index of 
    # value in dictionary into new list. if not in dictionary,
    # store value with its index as key and value 
    if data in dicta:
        new.append(([dicta[data],i]))
        # print(indices_list)
    else:
        dicta[numb[i]]=i
print(new)