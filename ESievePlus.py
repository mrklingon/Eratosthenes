# Python program to print all Primes Smaller
# than or equal to N using Sieve of Eratosthenes
#https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
from adafruit_circuitplayground import cp
import time
import random

blank = (0,0,0)
red = (20,0,0)
orange = (25, 10, 0)
yellow = (24,24,2)
green  = (0,20,0)
blue = (0,0,8)

def showbin(num):
    cp.pixels.fill(blue)
    if num != 0:
        for i in range(13):
            if i>9 and num >2**10:
                for m in range(9):
                        cp.pixels[m]=cp.pixels[m+1]
                cp.pixels[9] = blue
            if ((2**i)&num)>0:
                if i>9:
                    cp.pixels[9] = green
                else:
                    cp.pixels[i]= green
            time.sleep(.5)

    time.sleep(.5)

def showdigit(num):
    cp.pixels.fill(blue)
    for i in range(num):
        cp.pixels[i] = yellow
    time.sleep(1)

def shownum(num):
    snum = str(num)
    for i in range(len(snum)):
            showdigit(eval(snum[i]))


def pick():  # create a random color
    return (random.randrange(200), random.randrange(200), random.randrange(200))

def rndcolor():
    cp.pixels[random.randrange(10)] = pick()
    time.sleep(.1)

def isprime(val):
    global prime
    cell = int(val/8)
    bit = val - cell*8
    if prime[cell]&(2**bit) != 0:
        return True
    else:
        return False
 
def notprime(val):
    global prime
    cell = int(val/8)
    bit = val - cell*8
    if isprime(val):
        prime[cell] = prime[cell] ^ (2 ** bit)


def SieveOfEratosthenes(num):
    global prime
    prime = [255 for i in range(num+1)]
    notprime(1)
    notprime(0)
# boolean array
    p = 2
    while (p * p <= 8*num):

        # If prime[p] is not
        # changed, then it is a prime
        if (isprime(p) == True):
            rndcolor()
            # Updating all multiples of p
            for i in range(p * p, (8*num)+1, p):
                notprime(i)
        p += 1
        rndcolor()

    # Print all prime numbers
    for p in range(2, (8*num)+1):
        if isprime(p):
            print(p)
SieveOfEratosthenes(1000)
r=997

while True:
    if cp.button_a:
        r = random.randrange(8000)
        while (not isprime(r)):
            r = random.randrange(8000)
        showbin(r)
        time.sleep(1)
        print(r)
        shownum(r)
        time.sleep(1)
        cp.pixels.fill(blank)

    if cp.button_b:
        for p in range(2, 8000):
            if isprime(p):
                showbin(p)
                print(p)


    if cp.touch_A1:#last value of R
        showbin(r)
        time.sleep(1)
        print(r)
        shownum(r)
        time.sleep(1)
        cp.pixels.fill(blank)
