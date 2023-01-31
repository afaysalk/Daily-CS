import array
from contextlib import nullcontext
import logging

def palindrome(x):
     str1 = ""
     result = []
     for i in x:
        #i equals the list element directly
        #concatenates i with result , following this next line
        result = [i] + result
        #printing a list displays it entirely
        
     return (str1.join(result))

def delete_letter(array,character_to_delete):
     str1 = ""
     result = []
     for i in array:
        if i==character_to_delete:
            i=""
        result = result+ [i]        
     return (str1.join(result))     


#takes a wordlo
print("Type in a word :")
string=input()
print("Your word is :" + string)
#gets rid of spaces so it can work with phrases
string=string.replace(" ","")
#reverses the word
                                # this method is too easy but cool to have
                                # string_reverse=string[::-1]

#let's try implementing that ourselves

string_reverse=palindrome(string)




try:
    if string==string_reverse :
        print ("Yup, it's a palindrome alright")

    else :
        print("Nope, not a palindrome, not even close bucko")
except:
    logging.basicConfig(filename="log.log",encoding='utf-8',level=logging.DEBUG)
    logging.warning("Something ain't right chief")
