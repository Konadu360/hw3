# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# def inventory(loot):
#     kky={'gold coin': 42, 'rope': 1}
#     #loop through items in the list
#     for index,items in enumerate(loot):
#         print(index, items)

#         # check for value of items in kky and update
#         if items in kky:
#             kky[items]=kky[items]+1
            
#         else:
#                 kky.setdefault(items,1)
#     print('updated data=' , kky)
#     count=0
#     print('\ninventory:')

#     #loop through items in kky and count total items in stock
#     for key,val in kky.items():
#         print(val,key)
#         count=count+val
#     print('\ntotal items in inventory is %s '%(count))
    

# inventory(dragonLoot)

#OR


# def inventory(addeditems,loot):
#     for items in range(len(loot)):
#     # for index,items in enumerate(loot):
#         if loot[items] in addeditems:
#             # addeditems[items]=addeditems[items]+1
#             addeditems[loot[items]]=addeditems[loot[items]]+1
#         else:
#             # addeditems.setdefault(items,1)
#             addeditems.setdefault(loot[items],1)
#     return('updated data=' ,loot)
#     # print('inventory:')

# def displayInventory(addeditems):
#     count=0
#     for key,val in addeditems.items():
#         print(str(val)+ key)
#         count=count+val
#     print('total items in inventory is: '+ str(count))

# inv={'gold coin': 42, 'rope': 1} 
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']      
# inv =inventory(inv,dragonLoot)
# displayInventory(inv)



    
# import pprint

mydata=[
  {
    "metadata": None,
    "name": "kky",
    "properties": {
      "etag": "\"0x8D7D1A2F11B4680\"",
      "hasImmutabilityPolicy": "false",
      "hasLegalHold": "false",
      "lastModified": "2020-03-26T16:30:05+00:00",
      "lease": {
        "duration": None,
        "state": None,
        "status": None
      },
      "leaseDuration": None,
      "leaseState": "available",
      "leaseStatus": "unlocked",
      "publicAccess": "blob"
    }
  },
  {
    "metadata": None,
    "name": "kky-002",
    "properties": {
      "etag": "\"0x8D7D9CBD8E39CB1\"",
      "hasImmutabilityPolicy": "false",
      "hasLegalHold": "false",
      "lastModified": "2020-04-06T01:43:03+00:00",
      "lease": {
        "duration": None,
        "state": None,
        "status": None
      },
      "leaseDuration": None,
      "leaseState": "available",
      "leaseStatus": "unlocked",
      "publicAccess": None
    }
  }
]


# pprint.pprint(mydata)
# print('\n')

# for index,values in enumerate(mydata): 
#     dicti=values.get('properties',0)
#     pprint.pprint(dicti)
#     print('\n')
#     mydict={}
#     for key,val in dicti.items():
#         print(key,val)
#         mydict[key]=val
#     pprint.pprint(mydict)
# languages = ["Python", "C Programming", "Java", "JavaScript"]
# largest_string = max(languages,key=len)

# print("The largest string is:", largest_string)

# tableData = [['apples', 'oranges', 'cherries','banana'],
#              ['Alice','Bob', 'Carol','David'],
#              ['dogs', 'cats','goose', 'moose']]


# def table(group):
#     colwidths=[0] * len(group)
#     a=0
#     while a< len(group):
#         colwidths[a]=len(max(group[a],key=len))
#         a=a+1
#     print(colwidths)
#     for y in range(len(group[0])):
#         for x in range(len(colwidths)):
#             print(group[x][y].rjust(colwidths[x]),end=' ')
#         print(end='\n')
# table(tableData)
# print(range(len(tableData)))
# print('\n')
# print(len(max(tableData[2],key=len)))
# # for i in range(len(tableData)):
# #     print(i)
# print('\n')
# print((len(max(tableData,key=len)))) 
# colWidths = [0] * len(tableData)
# print(colWidths)
# a=0
# while a < len(tableData):
#     colWidths[a]=len(max(tableData[a],key=len))
#     a=a+1
# print(colWidths)
# for x in range(len(tableData[0])):
#     print(x)
# # print('\n')
#     # for y in range(len(colWidths)):
#     for y in range(len(tableData)):
#         print(tableData[y][x].rjust(10),end=' ')

# def printTable(tableData):
#     """
#     Print table neatly formatted:
#     e.g:

#     [['apples', 'oranges', 'cherries', 'banana'],
#     ['Alice', 'Bob', 'Carol', 'David'],
#     ['dogs', 'cats', 'moose', 'goose']]

#     becomes:

#       apples Alice  dogs
#      oranges   Bob  cats
#     cherries Carol moose
#       banana David goose
#     """
#     # make list of ints to store later max len element of each list
#     colWidths = [0] * len(tableData)

#     # Store maxlen of each list
#     i = 0
#     while i < len(tableData):
#         colWidths[i] = len(max(tableData[i], key=len))
#         i = i + 1

#     # Print formatted
#     for x in range(len(tableData[0])):
#         for y in range(len(colWidths)):
#             print(tableData[y][x].rjust(colWidths[y]), end=' ')
#         print(end='\n')

# printTable(tableData)
lst=[]
for i in range(0,100):
    print(i)
    lst.append(i)
print(lst)