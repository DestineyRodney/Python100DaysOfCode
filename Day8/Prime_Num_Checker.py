#Write your code below this line ๐

def prime_checker(number):
    isPrime = True
    for i in range(2, number):
        print(i)
        if number % i == 0:
            isPrime = False

    if isPrime == True:
        print(f"{number} is Prime")
    else:
        print(f"{number} is not Prime")

#Write your code above this line ๐

#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
