from hashlib import sha1
from fractions import gcd

def getH(M, q, b):
    # Get the SHA-1 Hash Value of M and truncate it to b bytes
    hashval = sha1(M).hexdigest()[0:b]
    h = int("0x"+hashval,0)
    if gcd(h, q-1) == 1:
        return hashval
    else:
        return getH(M+hashval, q, b)
