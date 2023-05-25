def area(height,base):
    area=height*base
    return area
print(area(20,10))


s=lambda a:a**3
m=s(5)
print(m)

def addition(*a):
    sum=0
    for i in a:
        sum=sum+i
    return sum
print(addition(2,3,4,5,6))