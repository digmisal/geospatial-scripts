for i in range(1,6):
    for j in range(i+1,6):
        print(" ",end=" ")
    for j in range(1,i+1):
         print("*",end=" ")
    for j in range(i-1,0,-1):
          print("*",end=" ")
    print()
