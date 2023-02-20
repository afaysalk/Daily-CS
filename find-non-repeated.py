

def check_unique(str) :
    for i in range(len(str)):
      for j in range(i+1,len(str)):
        if str[i]==str[j]:
           return False
    return True        



str = input ('Enter a word :')
if (check_unique(str)):
    print("Has unique character")

else : print("Doesn't have unique characters")
