#n, p, q, phi, d, e
#select prime number p, q
#n = p*q 
#select e,  n,e is coprime
#phi(n) = (p-1)*(q-1)
#de = 1mod(phi(n))
#(n,e) is public key
#d is private key

#encryption
#message = m
#c = pow(m, e, n)

#decryption
#message = pow(c, d, n)

#---bash---
#msieve -q n -> find p, q

#decryption ( c, n, d)
def readable(c) :
    m = hex(c).replace('0x','')
    m = m.replace('L','')
    m = m.decode('hex')
    return m

#n = 614010459838253953596498114943057697842675637887066261109163514805589167
#c = 416808431213057812839807235099929401146034654633863359116938353620975451
#d = 340035333160956238336074318075946961695270890880263371398510321485728225
#decryption (n, c, d)----------------
def ncd(n, c, d) :
    n = input('n -> ')
    c = open(enc, 'rb').read()
    c = int(c.encode('hex'),16)
    d = input('d -> ')
    m = pow(c, d, n)
    print m
    print readable(m)

#n = 783340156742833416191
#p = 27789079547
#q = 28188776653
#e = 653
#decryption (n, p, q, e)----------------
def npqe(n, p, q, e) :
    import gmpy
    n = p * q
    phi = (p-1) * (q-1)
    d = gmpy.invert(e, phi) # find d
    d = long(d)
    print d
    c = open(enc, 'rb').read()
    c = int(c.encode('hex'),16)
    m = pow(c, d, n)
    print m
    #print readable(m)
#----------------------------------
