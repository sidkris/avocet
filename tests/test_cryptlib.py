# tests/test_cryptlib.py

import unittest
from cryptlib.cryptlib import CryptLib

class TestCryptLib(unittest.TestCase):
    
    def test_caeser_cipher(self):
        # Test Caesar cipher with different shifts
        self.assertEqual(CryptLib.caeser_cipher('abc', 3), 'def')
        self.assertEqual(CryptLib.caeser_cipher('xyz', 3), 'abc')
        self.assertEqual(CryptLib.caeser_cipher('Hello, World!', 5), 'Mjqqt, Btwqi!')
        self.assertEqual(CryptLib.caeser_cipher('Hello, World!', -5), 'Czggj, Rjmgy!')
    
    def test_base64_encode_decode(self):
        # Test Base64 encoding and decoding
        original_text = 'Hello, World!'
        encoded_text = CryptLib.base_64_encode(original_text)
        decoded_text = CryptLib.base_64_decode(encoded_text)
        self.assertEqual(original_text, decoded_text)
    
    def test_hex_encode_decode(self):
        # Test Hex encoding and decoding
        original_text = 'Hello, World!'
        encoded_text = CryptLib.hex_encode(original_text)
        decoded_text = CryptLib.hex_decode(encoded_text)
        self.assertEqual(original_text, decoded_text)
    
    def test_xor_cipher(self):
        # Test XOR cipher encoding and decoding
        text = 'Hello, World!'
        key = 'key'
        encoded_text = CryptLib.xor_cipher_encode(text, key)
        decoded_text = CryptLib.xor_cipher_decode(encoded_text, key)
        self.assertEqual(text, decoded_text)
        
        # Test XOR cipher with a key of different length
        key = 'shortkey'
        encoded_text = CryptLib.xor_cipher_encode(text, key)
        decoded_text = CryptLib.xor_cipher_decode(encoded_text, key)
        self.assertEqual(text, decoded_text)
    
    def test_md5_hash(self):
        # Test MD5 hashing
        text = 'Hello, World!'
        expected_hash = '65a8e27d8879283831b664bd8b7f0ad4'
        self.assertEqual(CryptLib.md5_hash(text), expected_hash)
    
    def test_sha1(self):
        # Test SHA-1 hashing
        text = 'Hello, World!'
        expected_hash = '2ef7bde608ce5404e97d5f042f95f89f1c232871'
        self.assertEqual(CryptLib.sha1(text), expected_hash)
    
    def test_sha256(self):
        # Test SHA-256 hashing
        text = 'Hello, World!'
        expected_hash = 'a591a6d40bf420404a011733cfb7b190d62c65bf0d30e26e83b2d8a6f8e5421'
        self.assertEqual(CryptLib.sha256(text), expected_hash)
    
    def test_sha512(self):
        # Test SHA-512 hashing
        text = 'Hello, World!'
        expected_hash = 'b94d27b9934d3e08a52e52d7da7dabfa39b08a0d0f74e7c4c93d4b72d277e91bd10ef9c12e1d54b743c15e79d23e98ee8b4c05d77f1c749c7581ef574f96c09e'
        self.assertEqual(CryptLib.sha512(text), expected_hash)
    
    def test_sha3_256(self):
        # Test SHA-3 256 hashing
        text = 'Hello, World!'
        expected_hash = '7f783cbb251f1d9aebfb82a64e4d7854157c11e9068d46b55c0d5c53b84d2d7f'
        self.assertEqual(CryptLib.sha3_256(text), expected_hash)
    
    def test_sha3_512(self):
        # Test SHA-3 512 hashing
        text = 'Hello, World!'
        expected_hash = '7f783cbb251f1d9aebfb82a64e4d7854157c11e9068d46b55c0d5c53b84d2d7f02e37cdb19eb68d35c5d89bd947cd7ea7a9433d9d3b9c314b7e3e5a5d4c8f9db'
        self.assertEqual(CryptLib.sha3_512(text), expected_hash)
    
    def test_rsa_encode_decode(self):
        # Generate RSA keys for testing
        from Cryptodome.PublicKey import RSA
        from Cryptodome.Cipher import PKCS1_OAEP
        import base64
        
        # Generate a pair of RSA keys
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        text = 'Hello, World!'
        
        # Encrypt and decrypt the text
        encrypted_text = CryptLib.rsa_encode(text, public_key)
        decrypted_text = CryptLib.rsa_decode(encrypted_text, private_key)
        
        self.assertEqual(text, decrypted_text)

if __name__ == '__main__':
    unittest.main()
