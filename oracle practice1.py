'''
write a program that prints the numbers from 1 to 100. but for multiples of three
print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz"
'''
'''
i=1
while i <=100:
    #print (i)
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)
    i+=1
    '''

##2nd sloution
for i in range(1,101):
    if i % 3==0 and i % 5==0:
        print("FizzBuzz")
    elif i % 3==0:
        print("Fizz")
    elif i % 5==0:
        print("Buzz")
    else:
        print(i)



'''
Given values of two values n1 and n2 in a Binary search Tree,
find the lowest Common Ancestor (LCA). You may assume that both 
the values exist in the tree
'''
# A recursive python program to find LCA of two nodes
# n1 and n2

# A Binary tree node
'''

class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST


def lca(root, n1, n2):

	# Base Case
	if root is None:
		return None

	# If both n1 and n2 are smaller than root, then LCA
	# lies in left
	if(root.data > n1 and root.data > n2):
		return lca(root.left, n1, n2)

	# If both n1 and n2 are greater than root, then LCA
	# lies in right
	if(root.data < n1 and root.data < n2):
		return lca(root.right, n1, n2)

	return root

# Driver program to test above function


# Driver code
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)


# Function calls
n1 = 10
n2 = 14
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))

n1 = 14
n2 = 8
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))

n1 = 10
n2 = 22
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

total=0
for i in range(0, 101):
	total=i+total
print(total)
import random

correct_number = random.randint(1, 10)
print("I am thinking of a number between 1 and 10")
for i in range(1, 6):
	guess = int(input("take a guess: \n"))
	if guess<correct_number:
		print("your guess is too low")
	elif guess>correct_number:
		print("Your guess is too high")
	else:
		break
if guess ==correct_number:
	print("Good job! You guessed my number in ",str(i), "guesses!")
else:
	print("Nope. The number I was thinking of was ", str(i))
    '''

# """
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array 
# in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# """



Given_nums = [3,3,3,3,2,2,3,4,6,7,3,0,3,3,3,3]
val = 3
def kky(addo, kofi):
    i=0
    j=0
    while i<len(addo):
        if addo[i]!=kofi:
            addo[j]=addo[i]
            j+=1
        i+=1
    return addo[:j]
print(kky(Given_nums, 3))



# def array(num,inst):
#     i=0
#     while i<len(num):
#         if num[i]==inst:
#             del num[i]
#             continue
#         i+=1
#     return len(num), num
# print(array(Given_nums, val))


"""
Given a string and an integer k, you need to reverse the first k characters 
for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.
"""
# s = "abcdefgho0-ssa"
# k = 2
# data=list(s)
# i=0
# while i<len(data):
#     data[i:i+k]=reversed(data[i:i+k])
#     i=i+2*k
# print( ''.join(data))

# idea=''
# for i in range(0, len(s), 2*k):
#     chunk=s[i:i+2*k]
#     idea+=chunk[:k][::-1]+chunk[k:]
# print(idea)
    
''''
write a python fxn to parse a log file with entries in the format timestamp: message.
extract the timestamps and messages into separate sheet
'''

def parselog(logfile):
    message= {}
    timestamps =[]
    messages = []
    with open(logfile, "r") as f:
       for line in f:
           file=line.strip().split(": ", 1)
           message[file[0]]=file[1]
           timestamps.append(file[0].split(":", 1)[1])
           messages.append(file[1])

   
    with open('timestamps.txt', "w") as fel:
        for i in timestamps:
            fel.write(i)
    return timestamps, messages

print(parselog("logging.txt"))