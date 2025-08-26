import hashlib

password="hola123"
hash_file = hashlib.sha256(password.encode()).hexdigest()

print(hash_file)