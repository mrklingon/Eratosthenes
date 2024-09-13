# Eratosthenes
Circuit Playground code for finding Prime Numbers

* ESieve.js - MakeCode/Javascript for finding all primes < 1000 https://makecode.com/_H5qFx46rYF1c for Makecode version
* ESieve.py - CircuitPython for finding all primes < 1000 - copy to code.py
* ESievePlus.py - CircuitPython for finding all primes < 8000 - copy to code.py

All three of the above will flash colored lights while searching for the prime numbers. When done, A will pick a random prime and display it, first in binary, then digit-by-digit in decimal version. Pressing B will step through all of the primes if found, displaying in binary. Touch A1 to display the last random prime it found.



* neosieve.py - neotrinkey version (copy to code.py)
* ncount.py - support file for neosieve.py

NeoTrinkey version. It finds all primes < 1000. First it flashes colored lights while searching, then, when done, touching pad #1 will display a random prime digit by digit with binary coding. Touching pad #2 will redisplay the last random prime found.

All of the Circuit Python version (neotrinkey or Circuit Playground), if connected to Mu or a similar IDE, will print information to the REPL.


