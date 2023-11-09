#! /usr/bin/env python3

import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP


__author__ = 'Siddharth Krishnan'
__email__ = "sidkrishnan@protonmail.com"
__version__ = "1.0"
__license__ = "MIT"
__status__ = "Beta"

class Crypt:

  def caeser_cipher(self, text, shift):
    """
    Caeser Cipher encryption
    """
    cipher = ""
    for letter in text:
      if letter.isupper():
        cipher += chr((ord(letter) + shift - 65) % 26 + 65)
      elif letter.islower():
        cipher += chr((ord(letter) + shift - 97) % 26 + 97)
      else:
        cipher += letter
    return cipher

  def base_64_encode(self, text):
    """
    Base 64 encoding
    """
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")
    

  def base_64_decode(self, text):
    """
    Base 64 decoding
    """
    return base64.b64decode(text).decode('utf-8')


  def hex_encode(self, text):
    """
    Hex encoding    
    """
    return text.encode("utf-8").hex()

  def hex_decode(self, text):
    """
    Hex decoding
    """
    return bytes.fromhex(text).decode("utf-8")

  def xor_cipher_encode(self, text, key):
    """
    XOR Cipher encryption    
    """
    encoded_text = ""
  
    for i, char in enumerate(text):
      encoded_text += chr(ord(char) ^ ord(key[i % len(key)]))
  
    return encoded_text
  
  def xor_cipher_decode(self, text, key):
    """
    XOR Cipher decryption
    """
    decoded_text = ""
    
    for i, char in enumerate(text):
      decoded_text += chr(ord(char) ^ ord(key[i % len(key)]))
    return decoded_text


  def md5_hash(self, text):
    """
    MD5 hashing
    """
    return hashlib.md5(text.encode("utf-8")).hexdigest()
    
  
  def sha1(self, text):
    """Calculates the SHA-1 hash of a string."""
    hash_object = hashlib.sha1()
    hash_object.update(text.encode())
    return hash_object.hexdigest()
  
  def sha256(self, text):
    """Calculates the SHA-256 hash of a string."""
    hash_object = hashlib.sha256()
    hash_object.update(text.encode())
    return hash_object.hexdigest()
  
  def sha512(self, text):
    """Calculates the SHA-512 hash of a string."""
    hash_object = hashlib.sha512()
    hash_object.update(text.encode())
    return hash_object.hexdigest()

  def sha3_256(self, text):
    """Calculates the SHA-3 256 hash of a string."""
    hash_object = hashlib.sha3_256()
    hash_object.update(text.encode())
    return hash_object.hexdigest()

  def sha3_512(self, text):
    """Calculates the SHA-3 256 hash of a string."""
    hash_object = hashlib.sha3_512()
    hash_object.update(text.encode())
    return hash_object.hexdigest()

  # def aes_encode(self, text, key):
  #   """Encrypts a string using AES."""
  #   cipher_ = AES.new(key.encode(), AES.MODE_ECB)
  #   encrypted_text = cipher_.encrypt(text.encode())
  #   return base64.b64encode(encrypted_text)

  # def aes_decode(self, text, key):
  #   """Decrypts a string using AES."""
  #   cipher_ = AES.new(key.encode(), AES.MODE_ECB)
  #   decrypted_text = cipher_.decrypt(base64.b64decode(text))
  #   return decrypted_text.decode()

  def rsa_encode(self, text, public_key):
    """Encrypts a string using RSA."""
    public_key = RSA.importKey(public_key)
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_text = cipher.encrypt(text.encode())
    return base64.b64encode(encrypted_text)

  def rsa_decode(self, text, private_key):
    """Decrypts a string using RSA."""
    private_key = RSA.importKey(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher.decrypt(base64.b64decode(text))
    return decrypted_text.decode()

if __name__ == "__main__":
  print(Crypt().sha1(text = "Siddharth"))
  print(Crypt().sha256(text = "Siddharth"))
  print(Crypt().sha512(text = "Siddharth"))
  print(Crypt().sha3_256(text = "Siddharth"))
  print(Crypt().sha3_512(text = "Siddharth"))
  
