#Write a program that takes a string as input, and counts the frequency of each word in the string, there might
#be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
#highest-frequency word.

def Words_frequency (str1):

    dict1 = {}
    word = ''

    for i in range(len(str1)):
        #check until blank space so we know we have one word
        if str1[i] == ' ':

            #if word not in dict add it otherwise increase its frequency
            if word not in dict1:
                dict1[word] = 1
                word = ''
            else:
                dict1[word] = dict1[word] + 1 
                word = ''

        elif str1[i]==',':
            #checking for comma
            if word not in dict1:
                dict1[word] = 1
                word = ''
            else:
                dict1[word] = dict1[word] + 1 
                word = ''

        elif str1[i]=='.':
            #checking for full stop
            if word not in dict1:
                dict1[word] = 1
                word = ''
            else:
                dict1[word] = dict1[word] + 1 
                word = ''

        else:
            word = word + str1[i]
    #check for last as there will no space
    if word not in dict1:
        dict1[word] = 1
    else:
        dict1[word] = dict1[word] + 1

    # check dictionary for highest word frequency
    highest_freq = max(zip(dict1.values(), dict1.keys()))[0]

    return highest_freq


#Test cases
string1 = "write write write all the number from from from 1 to 100"

string2 = "if i was in sky then sky will be my land and land will be my sky, sky"
#explanation : in second string we are checking if string contains comma

string3 = "dog was behind cat or cat was behind. they might be running in circle"
#explanation : in second string we are checking if string contains full stop

print("Highest frequency\n",Words_frequency(string1))
print("Highest frequency\n",Words_frequency(string2))
print("Highest frequency\n",Words_frequency(string3))