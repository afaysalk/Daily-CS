""" give the first non repeated character in a stringd
give string
loop through each letter and all others
if you find one that's repeated, save it into a list
go through next letter, is it the same letter in the prviously saved array?
if not, compare it with other letters to see if it exists somewhere else
if not, pint that letter
"""



def repeat(word,array):
    for i in len(word):
        for k in len(array):
                if word[i]==array[k]:
                    check=False
                    break
        if check == False :
            print("Found letter already in the word")
            break            
        j=i
        for j in len(word):
            if word[i]==word[j]:
                word[i]=append(array)
                break
            else :
             print("Found it !")
             return


word='Juju Fitcat'
array=[]
repeat(word,array)             