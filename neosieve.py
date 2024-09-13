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
    pixels.fill(blank)

SieveOfEratosthenes(1000)
r=997


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
        r = random.randrange(1001)
        while (not prime[r]):
            r = random.randrange(1001)
        print(r)
        shownum(r)
        time.sleep(1)
        pixels.fill(blank)

    if Val == 2:
        print(r)
        shownum(r)
        time.sleep(1)
        pixels.fill(blank)
