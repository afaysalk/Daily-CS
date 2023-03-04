

def check(array):
   if sum(array)==(len(array)*(len(array)+1))/2 :
      return True
   else :
      return False 





array=[]
for i in range (100) :
    if i==60 :
      array.append(0)  
    else :
       array.append(i+1)
print(array)    
print(check(array))