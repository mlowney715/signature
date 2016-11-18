#!/usr/bin/python
# M. Phil Lowney - 01191051
# ECE-549 Network Security: Dr. Liu
# Homework #7 Problem 2
#
# sign.py - Attach a digital signature to a message

import argparse
import sys
import random
from getH import getH
from primitive_root import getPrimitiveRoot 
from fractions import gcd

# Input Parser
parser = argparse.ArgumentParser(description = "Digital Signature")
parser.add_argument("-d", "--debug", dest='DEBUG', help="Debugging Mode",
        action='store_true')
global args
args = parser.parse_args()

def isPrime(n):
    """Cloned from mhoc's github page"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for item in range(3,int(n/2)+1,2):
        if n % item == 0:
                return False
    return True

global primes
primes = [i for i in range(0,100) if isPrime(i)]

class key:
    def __init__(self):
        # Keep trying q values until there is a primitive root
        self.a = []
        while not self.a:
            try:
                self.q = random.choice(primes)
                self.a = getPrimitiveRoot(self.q)
            except OverflowError:
                # If there is an overflow error choose a different q
                self.__init__()
        self.a = self.a[0]
        # Private Key X is a random integer that is less than q
        self.X = random.randint(0,self.q-1)
        # Public Key Y
        self.Y = (self.a**self.X)%self.q

    def show(self):
        """Print Key Elements"""

        print("Public Elements: ")
        print("q = "+str(self.q))
        print("a = "+str(self.a))
        print
        print("Private Key X = "+str(self.X))
        print("Public Key Y  = "+str(self.Y))

    def sign(self,M):
        """Sign a message"""

        # Get the hash value for the message
        h = int("0x"+getH(M, self.q, 2),0)
        Z = (self.X%(self.q-1))/float(h)
        sig = (self.a**Z)**h
        if args.DEBUG:
            print("Z: "+str(Z))
            print("sig: "+str(sig))
        return sig
            


def main():
    k = key()
    print("Generating your public and private key")
    if args.DEBUG:
        k.show()
    M = raw_input("What is your message: ")
    print("Attaching your signature...")
    sig = k.sign(M)
    print("Signed.")
    print
    print("Verifying...")
    print("Public Key Y = "+str(k.Y))
    print("Signature mod q = "+str(sig%k.q))
    print("Done.")

if __name__ == "__main__":
    main()

