
#print prime numbers in range
for num in range(100,2000+1):
    flag=True
    for i in range(2,num):
        if num % i==0:
            flag=False
            break
    if flag:
        print(num,end=" ") 
#print Armstrong number in range 
for num in range(100,2000+1):
      temp=num
      length=len(str(num))
      sum_val=0
      while temp > 0:
           rem =temp % 10
           sum_val +=rem **length
           temp //=10
      if sum_val==num:
               print(num,end=" ")
          

