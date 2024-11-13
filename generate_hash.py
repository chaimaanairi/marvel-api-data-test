import hashlib
import time

# Your public and private keys
public_key = '25dc2a8ba6477fd6faf4788a1d51f4f2'
private_key = 'b7c49faadee8c8a9054ff34b2839ba9fddd2edeb'


def generate_hash():
    # Get the current timestamp (could be any random number or timestamp)
    ts = str(int(time.time()))

    # Create the hash (MD5 of timestamp + private key + public key)
    hash_input = ts + private_key + public_key
    hash_value = hashlib.md5(hash_input.encode('utf-8')).hexdigest()

    return ts, hash_value
