"""rsa_free.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import math

def encrypt(msg, p, q, e):
    """Encrypts a message using RSA encryption algorithm.

    Args:
        message (int): The message to be encrypted.
        p (int): The first prime number.
        q (int): The second prime number.
        e (int): The encryption exponent.

    Returns:
        int: The encrypted message.
    """

    n = p * q
    enc_msg = pow(msg, e, n)
    return enc_msg


if __name__ == '__main__':
    message = int(input("Enter the message to be encrypted: "))

    p = 11
    q = 7
    e = 3

    print("Original Message is:", message)
    encrypted_message = encrypt(message, p, q, e)
    print("Encrypted Message is:", encrypted_message)
