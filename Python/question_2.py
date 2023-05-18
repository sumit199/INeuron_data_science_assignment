#Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
#he can remove just one character at the index in the string, and the remaining characters will occur the same
#number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .

def Check_string (str1):

    dict1 = {}
    flag = 0

    for i in str1:
        #
        if i in dict1:
            
            if dict1[i]>2:
                return 'No'
            else:
                dict1[i] = dict1[i]+1
                flag += 1 #if two char repeated mmore than once than string is invalid

            if flag>1:
                return 'No'
        else:
            dict1[i] = 1

    return 'Yes'

s1 = "abc"
s2 = "abccc"
s3 = "abbc"
#chceking if removing one character can validate string
s4 = "aabbc"
#checking if it can handle two chararcters repeating twice

print(Check_string(s1))
print(Check_string(s2))
print(Check_string(s3))
print(Check_string(s4))