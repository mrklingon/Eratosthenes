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
        for i in range(10):
            if ((2**i)&num)>0:
                cp.pixels[i] = green
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

def SieveOfEratosthenes(num):
    global prime
    prime = [True for i in range(num+1)]
# boolean array
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
            rndcolor()
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        rndcolor()
        p += 1
 
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            print(p)
 
SieveOfEratosthenes(1000)
r=997

while True:
    if cp.button_a:
        r = random.randrange(1001)
        while (not prime[r]):
            r = random.randrange(1001)
        showbin(r)
        time.sleep(1)
        print(r)
        shownum(r)
        time.sleep(1)
        cp.pixels.fill(blank)
        
    if cp.button_b:
        for p in range(2, 1001):
            if prime[p]:
                showbin(p)
                print(p)
   
  
    if cp.touch_A1:#last value of R
        showbin(r)
        time.sleep(1)
        print(r)
        shownum(r)
        time.sleep(1)
        cp.pixels.fill(blank)
        
