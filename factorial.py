
num=int(input("enter a number: "))

factorial=1
if num<0:
    print("Factorial cannot be calculated for negative values")
elif num==0:
    print("The Factorial of zero is 1")
else:
     while num>0:
        factorial=factorial*num
        num=num-1
     print("The Factorial is",factorial) 

