import unittest
from main import VigenereCipher


class VigenereTestCase(unittest.TestCase):
    def setUp(self):
        self.cipher=VigenereCipher("TRAIN","ENCODEINPYTHON")
    def test_init(self):
        self.assertEqual(self.cipher.keyword,"TRAIN")
    def test_init_validation(self):
        self.assertRaises(TypeError, VigenereCipher.__init__, 220,220)
        self.assertRaises(ValueError,VigenereCipher,"$%a","$$$")
    def test_extend_keyword(self):
        self.cipher.extend_keyword(12)
        self.assertEqual(self.cipher.realKeyword,"TRAINTRAINTR")
    def test_cipher(self):
        response=self.cipher.cipher()
        self.assertEqual(response,"X_CWQXZNXfgYOV")
if __name__ == '__main__':
    unittest.main()
