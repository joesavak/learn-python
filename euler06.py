
def sum_of_squares(num):
    sum=0
    for y in range (1,num+1):
        sum=sum+(y**2)
    return sum

def square_of_sums(num):
    sum=0
    for y in range(1,num+1):
        sum+=y
    return sum**2

print(square_of_sums(100)-sum_of_squares(100))
