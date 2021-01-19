""" 
Write a function that takes a string as input and reverse only the vowels of a string
"""
Inputa= "leetcode"

#define function to execute code
def reverse(data):
    vowels='aeiouAEIOU'
    vows_only=''
    conso_only=''

    #loop through string and store vowels and consonants separately
    for i in data:
        if i in vowels:
            vows_only+=i
        else:
            conso_only+=i

    #reverse vowels stored
    vows_only=vows_only[::-1]
    i=0
    v_count=0
    c_count=0
    reversed_vowels=''

    #loop through the data and check if item in vowels
    #append items in vows_only and conso_only to reversed_vowels

    while i < len(data):
        if data[i] in vowels:
            reversed_vowels+=vows_only[v_count]
            v_count+=1
        else:
            reversed_vowels+=conso_only[c_count]
            c_count+=1
        i+=1
    return reversed_vowels

print(reverse(Inputa))

def rev(s):
    s=list(s)
    vowels_dict={}
    vowels='AIEOUaieou'
    for i,j in enumerate(s):
        if j in vowels:
            vowels_dict[i]=j
    data=zip(sorted(vowels_dict.keys(),reverse=True),vowels_dict.values())
    for k,l in data:
        print(k,l)
        s[k]=l
    return ''.join(s)

    




















    # vowels='aeiouAIEOU'
    # s=list(s)
    # vowels_dict={}
    # for i, j in enumerate(s):
    #     if j in vowels:
    #         vowels_dict[i]=j
    # data=zip(sorted(vowels_dict.keys(),reverse=True), vowels_dict.values())
    # for k, v in data:
    #     s[k] = v
    #     print(s)
    # return ''.join(s)
print(rev(Inputa))