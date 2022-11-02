import unittest

from translator import english_to_french, french_to_english

class EngToFrTester(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNone(english_to_french())

class FrtoEngTester(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNone(french_to_english())

unittest.main()