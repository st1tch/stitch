#https://github.com/ctfs/write-ups-2014/tree/master/hack-lu-ctf-2014/wiener
import sys
import base64
import struct
import math
import fractions
import gmpy
import sympy

import pyasn1_modules.rfc3447
import pyasn1.codec.ber.encoder

sys.path.append("/home/stitch/machome/rsa/rsa-wiener-attack")
import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

#input public key:
def hack_RSA(e,n):
  '''
  Finds d knowing (e,n)
  applying the Wiener continued fraction attack
  '''
  frac = ContinuedFractions.rational_to_contfrac(e, n)
  convergents = ContinuedFractions.convergents_from_contfrac(frac)

  for (k,d) in convergents:

    #check if d is actually the key
    if k!=0 and (e*d-1)%k == 0:
      phi = (e*d+1)//k
      s = n - phi + 1
      # check if the equation x^2 - s*x + n = 0
      # has integer roots
      discr = s*s - 4*n
      if(discr>=0):
        t = Arithmetic.is_perfect_square(discr)
        if t!=-1 and (s+t)%2==0:
          print("Hacked!")
          return d,phi

def test_hack_RSA(e,n):
  print("Testing Wiener Attack")
  times = 1

  while(times>0):
    #e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
    print("(e,n) is (", e, ", ", n, ")")

    hacked_d = hack_RSA(e, n)

    print("hacked_d = ", hacked_d)
    print("-------------------------")
    times -= 1

  return hacked_d

def asn1_encode_priv_key(N, e, d, p, q):
  key = pyasn1_modules.rfc3447.RSAPrivateKey()
  dp = d % (p - 1)
  dq = d % (q - 1)
  qInv = gmpy.invert(q, p)
  #assert (qInv * q) % p == 1
  key.setComponentByName('version', 0)
  key.setComponentByName('modulus', N)
  key.setComponentByName('publicExponent', e)
  key.setComponentByName('privateExponent', d)
  key.setComponentByName('prime1', p)
  key.setComponentByName('prime2', q)
  key.setComponentByName('exponent1', dp)
  key.setComponentByName('exponent2', dq)
  key.setComponentByName('coefficient', qInv)
  ber_key = pyasn1.codec.ber.encoder.encode(key)
  pem_key = base64.b64encode(ber_key).decode("ascii")
  out = ['-----BEGIN RSA PRIVATE KEY-----']
  out += [pem_key[i:i + 64] for i in range(0, len(pem_key), 64)]
  out.append('-----END RSA PRIVATE KEY-----\n')
  out = "\n".join(out)
  return out.encode("ascii")

if __name__ == "__main__":
  sys.setrecursionlimit(1500)

  keydata = base64.b64decode(sys.argv[1])

  parts = []
  while keydata:
    # read the length of the data
    dlen = struct.unpack('>I', keydata[:4])[0]

    # read in <length> bytes
    data, keydata = keydata[4:dlen+4], keydata[4+dlen:]

    parts.append(data)

  e_val = eval('0x' + ''.join(['%02X' % struct.unpack('B', x)[0] for x in
      parts[1]]))
  n_val = eval('0x' + ''.join(['%02X' % struct.unpack('B', x)[0] for x in
      parts[2]]))

  print hex(e_val)

  d_val, phi_val = test_hack_RSA(e_val, n_val)
  #d_val = 724746542590011388513367385228693742222740657137483753552318433232068370338961145215199994578740789016238655979015224570943L
  #phi_val = 338630205260455689413627911306068443537112802550361922213620660503310212139001530156458392949653034244789612680980241965923780722889133495349537107789761426092510299239678696031652780059016898519278860185536978111680123402473365833456785718098200501968322228116681190425490850863660038143310790555506293106612832752816526294946244330554558811312381169746599669997187914877490856336218310169927726408740994026774015446804415510971495034414170679517574320170326096806247477803294330492724911633596245761058343100118785517282649648198386928412053124797987039344718844068821755346442016872442675863694586221009879142600L

  print("n:%s\n"% n_val)
  print("e:%s\n"% e_val)
  print("d:%s\n"% d_val)
  print("phi:%s\n"% phi_val)

  p_val = sympy.Symbol('p_val')
  eq = sympy.Eq(p_val*p_val + (n_val+1-phi_val)*p_val + n_val)
  solved = sympy.solve(eq, p_val)

  p_val = int(-1*(solved[0]))
  q_val = int(-1*(solved[1]))

  print n_val == p_val*q_val

  print("p:%s\n"% p_val)
  print("q:%s\n"% q_val)

  print repr(p_val)
  print type(p_val)
  print asn1_encode_priv_key(n_val, e_val, d_val, p_val, q_val)
