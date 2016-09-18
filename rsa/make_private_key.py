import pyasn1_modules.rfc3447
import pyasn1.codec.ber.encoder
import os
import gmpy
import base64
import math
import fractions
import sympy

def asn1encodeprivkey(N, e, d, p, q):
    key = pyasn1_modules.rfc3447.RSAPrivateKey()
    dp = d % (p - 1)
    dq = d % (q - 1)
    qInv = gmpy.invert(q, p)
    assert (qInv * q) % p == 1
    key.setComponentByName('version', 0)
    key.setComponentByName('modulus', N)
    key.setComponentByName('publicExponent', e)
    key.setComponentByName('privateExponent', d)
    key.setComponentByName('prime1', p)
    key.setComponentByName('prime2', q)
    key.setComponentByName('exponent1', dp)
    key.setComponentByName('exponent2', dq)
    key.setComponentByName('coefficient', qInv)
    berkey = pyasn1.codec.ber.encoder.encode(key)
    pemkey = base64.b64encode(berkey).decode("ascii")
    print pemkey
    out = ['-----BEGIN RSA PRIVATE KEY-----']
    out += [pemkey[i:i + 64] for i in range(0, len(pem_key), 64)]
    out.append('-----END RSA PRIVATE KEY-----\n')
    out = "\n".join(out)
    return out.encode("ascii")

b = ['N','e','d','p','q']
a = map(long, [raw_input("input %c -> "%b[i]) for i in range(len(b))])

result = asn1encodeprivkey(a[0], a[1], a[2], a[3], a[4])
open('private.key','wb').write(result)
os.chmod('private.key', int('0600', 8))
