for i in range(7,0,-1):
    for j in range(i,6+1):
        print(" ",end=" ")
    for j in range(i-1):
         print("*",end=" ")
    for j in range(i,0,-1):
          print("*",end=" ")
    print()
