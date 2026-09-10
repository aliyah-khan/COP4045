import unittest
from p5_Khan_Aliyah import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):

    def test_cipher(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor")

    def test_cipher_uppercase(self):
        self.assertEqual(caesar_cipher("Hello World!", 3), "Khoor Zruog!")

    def test_cipher_wraparound(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc")

    def test_cipher_negative_shift(self):
        self.assertEqual(caesar_cipher("abc", -3), "xyz")


class TestCaesarDecipher(unittest.TestCase):

    def test_decipher(self):
        encrypted = caesar_cipher("Hello World!", 5)
        self.assertEqual(caesar_decipher(encrypted, 5), "Hello World!")


class TestLetterFrequency(unittest.TestCase):

    def test_frequency(self):
        result = letter_frequency("Hello!")
        self.assertEqual(result["h"], 1)
        self.assertEqual(result["e"], 1)
        self.assertEqual(result["l"], 2)
        self.assertEqual(result["o"], 1)

    def test_ignores_spaces_and_symbols(self):
        result = letter_frequency("A B-C!")
        self.assertEqual(result["a"], 1)
        self.assertEqual(result["b"], 1)
        self.assertEqual(result["c"], 1)
        self.assertEqual(result["d"], 0)


if __name__ == "__main__":
    unittest.main()
