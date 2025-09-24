#Parz tveri xndiry

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

for num in range(a,b+1):
    is_prime = True
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                is_prime=False
        if is_prime:
            print("Parz tiv: ", num)