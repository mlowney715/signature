#######################################
#                                     #
# Primitive Root (2014.06.15)         #
#                                     #
# Cokie(Jinwoong Choi)                # 
#                                     # 
# https://github.com/cokiencoke       #
#                                     #
#######################################

import time,math
def integerFactorization(n):
    data = {}
    i = 2
    while 1:
        if n % i == 0 :
            if i in data :
                data[i] += 1
            else :
                data[i] = 1
            n = n / i
            i = 2
            if n == 1 :
                break
        else :
            i+=1 

    return data
    
def getNumberOfPrimitiveRoot(n):
    for i in range(2):
        data = integerFactorization(n)
        n = 1
        for k in data :
            n *= int(math.pow(k,data[k]) - math.pow(k,data[k]-1))
    return n

def getPrimitiveRoot(n):
    intFactor = integerFactorization(n)
    data = {}
    result = []
    isSkip = 0
    for i in range(1,n):
        for j in intFactor :
            if i%j==0 :
              isSkip = 1
              break
        if isSkip == 1:
            isSkip = 0
            continue
        
        data[i] = {}
        j = 0
        while 1:
            num = math.pow(i,j) % n
            if num in data[i] :
                break
            data[i][num] = 0
            j+=1

    for k in data :
        if len(data[k])==len(data) :
            result.append(k)

    return result

def isItHasPrimitiveRoot(n) :
    data = integerFactorization(n)
        
    if len(data) == 1 :
        return True

    p = data.keys()[-1]
    if n == 2 or n == 4 or 2*math.pow(p,data[p]) == n:
        return True
    else :
        return False
