


def palindrome(str):
    j=len(str)
    if (j%2!=0) :
        return False
    for i in range(len(str)):
        if str[i]!=str[j-1-i]:
            return False
    return True

string = input('Give a word')

if palindrome(string):
    print("It's a palindrome")
else: print("Not a palindrome")   