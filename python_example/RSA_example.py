from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
public_key = key.publickey()
pub_key2 = key.publickey().exportKey("PEM")

priv_key2 = key.exportKey("PEM")
priv_key = RSA.importKey(priv_key)

enc_data = public_key.encrypt('abcdefgh', 32)
key.decrypt(enc_data)
