from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

def fetch_public_key(user):
    with open(user.decode('ascii') + "key.pub", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend())
    return public_key

message = b"Nelson likes cats."

signature = b'*\xff\xdd\xcf\xf7\x96\x92?6\xdbs*pw\xf9+\x85\xc5D\xd8\xfd\xd2\xcc\\<8w\xc5\x04\xb0\x8fU\xe2\xa4\xd2\xba\xb22:z\xbe(\r\xb6*\xa0e\xb4\xc0\x04\xb1\xa5\x91\xdc\\\x13\x89\xec\xc8X!U\x94\xbf<\xf7\x0e\xb3\xfc\x84e`P\x88\x06\xe4\x89\xae;\xf3\x1f\xdd\xfb\xee;;\xb9\x03\x14\x14S\nu>\xe3\x8a\xb1\x0c\xc5R\xd1S@3B\x0b\xd9\xa9u\xfd\xb6\xe1\xca\xef\x86(\xa6\x19\xbegH\xa7\x81\x8fFg\xb1`'

user = message.split()[0].lower()

public_key = fetch_public_key(user)

public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("Message verification succeeded!")
