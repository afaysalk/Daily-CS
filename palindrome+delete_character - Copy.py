
#usually given to see if you know recursion
#still not perfect, doesn't really work that well

def swap(s,a,b):
  s[a], s[b] = s[b], s[a]
  return s


def perms(s,f):
  # i is position, v is value
  for i,v in enumerate(s):
    if(len(s)==f): return 
    new=swap(s,f,i)
    print(new)
    f+=1
    perms(s,f)
    

print("Give a word :")
word=input()
f=0
word=list(word)
perms(word,f)