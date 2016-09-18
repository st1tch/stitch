import os, base64
from pyasn1.type import univ
from pyasn1.codec.der import encoder, decoder

################################################################################

# parse id_rsa and convert to a more workable format.
f = open('id_rsa', 'r').read()
f = ''.join(l for l in f.split('\n') if l and not l.startswith('-----'))
f = base64.b64decode(f)

dec = decoder.decode(f)
_, n, e, d, p, q, dp, dq, qi = map(int, dec[0])
print('decoded asn1.')

################################################################################

import RecoverPrimeFactors_Ned as prime

_str = 'n = ' + str(n) + '\n\n\n'
_str += 'e = ' + str(e) + '\n\n\n'
_str += 'd = ' + str(d) + '\n\n\n'
open('ned.txt','wb').write(_str)
print type(n),type(e),type(d)
p, q = prime.RecoverPrimeFactors(int(n),int(e),int(d))
print('\x1b[32mp = {:#x}\x1b[0m'.format(p))
print('\x1b[32mq = {:#x}\x1b[0m'.format(q))

################################################################################

# fix key.
d = d % lcm(p - 1, q - 1)
print('\x1b[32md := {:#x}\x1b[0m'.format(d))
p = q = 1
dp = dq = qi = 0

################################################################################

# encode new key.
key = ''
k = univ.SequenceOf(univ.Integer()).setComponents(0, n, e, d, p, q, dp, dq, qi)
enc = base64.b64encode(encoder.encode(k)).decode()
key += '-----BEGIN RSA PRIVATE KEY-----\n'
for i in range(0, len(enc), 64):
	key += enc[i:i+64] + '\n'
key += '-----END RSA PRIVATE KEY-----\n'

open('id_rsa.good', 'w').write(key)
os.chmod('id_rsa.good', int('0600', 8))
