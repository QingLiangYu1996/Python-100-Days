from math import sqrt
for num in range (2,1000):
    is_prime=True
    for i in range(2,int(sqrt(num)+1)):
        if num%i==0:
            is_prime=False
            break
    if is_prime and num!=1:
        print(num,end='\n')
    