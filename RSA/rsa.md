# RSA key generator

```python
"""RSA key generator"""

import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

keyPair = RSA.generate(4043)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

#encryption
MSG = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(MSG)
print("Encrypted:", binascii.b2a_hex(encrypted))
```
