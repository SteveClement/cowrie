# Copyright (c) 2009-2014 Upi Tamminen <desaster@gmail.com>
# See the COPYRIGHT file for more information

"""
This module contains ...
"""


import os

from twisted.conch.ssh import keys
from twisted.python import log

from cowrie.core.config import CowrieConfig


def getRSAKeys():
    publicKeyFile: str = CowrieConfig.get("ssh", "rsa_public_key")
    privateKeyFile: str = CowrieConfig.get("ssh", "rsa_private_key")
    if not (os.path.exists(publicKeyFile) and os.path.exists(privateKeyFile)):
        log.msg("Generating new RSA keypair...")
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives.asymmetric import rsa

        rsaKey = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )
        publicKeyString = keys.Key(rsaKey).public().toString("openssh")
        privateKeyString = keys.Key(rsaKey).toString("openssh")
        with open(publicKeyFile, "w+b") as f:
            f.write(publicKeyString)
        with open(privateKeyFile, "w+b") as f:
            f.write(privateKeyString)
    else:
        with open(publicKeyFile, "rb") as f:
            publicKeyString = f.read()
        with open(privateKeyFile, "rb") as f:
            privateKeyString = f.read()
    return publicKeyString, privateKeyString


def getDSAKeys():
    publicKeyFile: str = CowrieConfig.get("ssh", "dsa_public_key")
    privateKeyFile: str = CowrieConfig.get("ssh", "dsa_private_key")
    if not (os.path.exists(publicKeyFile) and os.path.exists(privateKeyFile)):
        log.msg("Generating new DSA keypair...")
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives.asymmetric import dsa

        dsaKey = dsa.generate_private_key(key_size=1024, backend=default_backend())
        publicKeyString = keys.Key(dsaKey).public().toString("openssh")
        privateKeyString = keys.Key(dsaKey).toString("openssh")
        with open(publicKeyFile, "w+b") as f:
            f.write(publicKeyString)
        with open(privateKeyFile, "w+b") as f:
            f.write(privateKeyString)
    else:
        with open(publicKeyFile, "rb") as f:
            publicKeyString = f.read()
        with open(privateKeyFile, "rb") as f:
            privateKeyString = f.read()
    return publicKeyString, privateKeyString


def getECDSAKeys():
    publicKeyFile: str = CowrieConfig.get("ssh", "ecdsa_public_key")
    privateKeyFile: str = CowrieConfig.get("ssh", "ecdsa_private_key")
    if not (os.path.exists(publicKeyFile) and os.path.exists(privateKeyFile)):
        log.msg("Generating new ECDSA keypair...")
        from cryptography.hazmat.primitives.asymmetric import ec

        ecdsaKey = ec.generate_private_key(ec.SECP256R1())
        publicKeyString = keys.Key(ecdsaKey).public().toString("openssh")
        privateKeyString = keys.Key(ecdsaKey).toString("openssh")
        with open(publicKeyFile, "w+b") as f:
            f.write(publicKeyString)
        with open(privateKeyFile, "w+b") as f:
            f.write(privateKeyString)
    else:
        with open(publicKeyFile, "rb") as f:
            publicKeyString = f.read()
        with open(privateKeyFile, "rb") as f:
            privateKeyString = f.read()
    return publicKeyString, privateKeyString


def geted25519Keys():
    publicKeyFile: str = CowrieConfig.get("ssh", "ed25519_public_key")
    privateKeyFile: str = CowrieConfig.get("ssh", "ed25519_private_key")
    if not (os.path.exists(publicKeyFile) and os.path.exists(privateKeyFile)):
        log.msg("Generating new ed25519 keypair...")
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

        ed25519Key = Ed25519PrivateKey.generate()
        publicKeyString = keys.Key(ed25519Key).public().toString("openssh")
        privateKeyString = keys.Key(ed25519Key).toString("openssh")
        with open(publicKeyFile, "w+b") as f:
            f.write(publicKeyString)
        with open(privateKeyFile, "w+b") as f:
            f.write(privateKeyString)
    else:
        with open(publicKeyFile, "rb") as f:
            publicKeyString = f.read()
        with open(privateKeyFile, "rb") as f:
            privateKeyString = f.read()
    return publicKeyString, privateKeyString
