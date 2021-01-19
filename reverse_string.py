"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.
"""

s = "abcdefgho0-ssa1"
k = 2

#define function to execute code
def reverse(data,d):
    i=0
    data=list(data)

    #loop through list and for every 2k char, reverse 1st two chars
    while i<len(data):
        data[i:i+d]=reversed(data[i:i+d])
        i+=2*d
        
    #return string of data
    return ''.join(data)

print(reverse(s,k))
