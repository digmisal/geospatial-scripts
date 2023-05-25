

for i in range (1,101):
    x=0
    for j in range(1,i+1):
        if i%j==0:
            x=x+1
    if x==2:
        print(i)   


     
