#prime number checker

def prime_check(num):
    f=0
    for i in range(2,int(num**(1/2))+1):
        if(num%i == 0):
            f=1
            print(f"{num} is not a prime number.")
            break
    if(f==0):
        print(f"{num} is a prime number.")
     
n = int(input("ENTER THE NUMBER YOU WANT TO CHECK :"))
prime_check(n)