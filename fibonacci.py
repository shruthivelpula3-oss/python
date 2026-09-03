#program for fibonocci series
n=int(input("enter range"))
num1,num2=0,1
print(num1,num2,end=' ')
for i in range(2,n):
      num=num1+num2
      print(num,end=" ")
      num1,num2=num2,num
      
