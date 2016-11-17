#!/usr/bin/python
# M. Phil Lowney - 01191051
# ECE-549 Network Security: Dr. Liu
# Homework #7 Problem 2
#
# sign.py - Attach a digital signature to a message

import argparse
import sys
import random
import hashlib
from fractions import gcd
from primitive_root import getPrimitiveRoot 

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
primes = [i for i in range(0,200) if isPrime(i)]

class key:
    def __init__(self):
        # self.a = next(i for i in range (0,self.q-1) if gcd(i,self.q) == 1)
        self.a = []
        while not self.a:
            self.q = random.choice(primes)
            self.a = getPrimitiveRoot(self.q)
        self.a = self.a[0]
        self.X = random.randint(0,self.q-1)
        self.Y = (self.a**self.X)%self.q

    def show(self):
        print("Public Elements: ")
        print("q = "+str(self.q))
        print("a = "+str(self.a))
        print
        print("Private Key X = "+str(self.X))
        print("Public Key Y  = "+str(self.Y))

    def sign(self,M):
        m = hashlib.sha1()
        m.update(M)
        h = int("0x"+m.hexdigest(), 0)
        while gcd(h,self.q-1) != 1:
            m.update(m.digest())
            h = int("0x"+m.hexdigest(), 0)
        if args.DEBUG:
            print("X: "+str(self.X))
            print("q-1: "+str(self.q-1))
            print("h: "+str(h))
        Z = float((self.X%(self.q-1))/h)
        sig = self.a**Z
        if args.DEBUG:
            print("Z: "+str(Z))
            print("sig: "+str(sig))
        return (sig, h)
            


def main():
    k = key()
    print("Generating your public and private key")
    if args.DEBUG:
        k.show()
    M = raw_input("What is your message: ")
    print("Attaching your signature...")
    (sig, h) = k.sign(M)
    print("Signed.")
    print
    print("Verifying...")
    print("Public Key Y = "+str(k.Y))
    print("Signature**hash = "+str(sig**h))
    print("Done.")

if __name__ == "__main__":
    main()

