# Python program to print all Primes Smaller
# than or equal to (bits * 1000) using Sieve of Eratosthenes
#https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
#An array of 1000 numbers of "bits" length are used to calculate 

import time
import random
import neopixel
import board
import touchio

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

from ncount import  *



blank = (0,0,0)
red = (20,0,0)
orange = (25, 10, 0)
yellow = (24,24,2)
green  = (0,20,0)
blue = (0,0,8)

def pick():  # create a random color
    return (random.randrange(200), random.randrange(200), random.randrange(200))

def rndcolor():
    pixels[random.randrange(4)] = pick()
    time.sleep(.1)

def shownum(num):
    snum = str(num)
    for i in range(len(snum)):
            binnum(eval(snum[i]),green)
            time.sleep(.2)

bits = 29

def isprime(val):
    global prime
    cell = int(val/bits)
    bit = val - cell*bits
    if prime[cell]&(2**bit) != 0:
        return True
    else:
        return False
 
def notprime(val):
    global prime
    cell = int(val/bits)
    bit = val - cell*bits
    if isprime(val):
        prime[cell] = prime[cell] ^ (2 ** bit)


def SieveOfEratosthenes(num):
    global prime
    prime = [(512+256+255) for i in range(num+1)]
    notprime(1)
    notprime(0)
# boolean array
    p = 2
    while (p * p <= bits*num):

        # If prime[p] is not
        # changed, then it is a prime
        if (isprime(p) == True):
            rndcolor()
            # Updating all multiples of p
            for i in range(p * p, (bits*num)+1, p):
                notprime(i)
        p += 1
        rndcolor()
    primecount = 0
    # Print all prime numbers
    for p in range(2, (bits*num)+1):
        if isprime(p):
            print(p)
            primecount = primecount + 1
    for i in range(4):
        pixels[i] = blank
        time.sleep(.1)
    print ("found "+str(primecount)+ " numbers")
    
    
SieveOfEratosthenes(1000)
r=3


touched = time.monotonic()

while True:
    Val = 0
    if time.monotonic() - touched < 0.15:
        continue
    if touch1.value:

        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()

    if Val == 1:
        r = random.randrange(10001)
        while (not isprime(r)):
            r = random.randrange(10001)
        print(r)
        shownum(r)
        time.sleep(1)
        pixels.fill(blank)

    if Val == 2:
        print(r)
        shownum(r)
        time.sleep(1)
        pixels.fill(blank)
