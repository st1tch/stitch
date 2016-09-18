import time
import sys

def rwh(n):
    t1 = time.time()
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    print 'time =', str(time.time() - t1) 
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def main():
    print sum(rwh(int(sys.argv[1])))

if __name__ == '__main__':
    main()
