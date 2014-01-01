found =0
keep =0
#optimization: lots of string casts that could be costly. Maybe faster way to check palindrome?
for x in range(100,999):
    for y in range (100,999):
        product=x*y
        if str(product) == str(product)[::-1]:
            found=product
            break
    if found>keep:
            keep=found
    
print(keep)
