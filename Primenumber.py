def is_prime(number):
    #check if the number is less than 2
    if number < 2:
        return False
    #Check for factors from 2 to square root of the number
    for i in range(2,int(number**0.5)+1):
        if number %i==0:
            #If factor is found,the number is not prime
            return False
    return True

num=int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is a not a prime number")