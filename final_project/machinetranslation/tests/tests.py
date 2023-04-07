import unittest
from translator import englishtofrench, frenchtoenglish

class Testing(unittest.TestCase):
    def test_englishtofrench(self):
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertNotEqual(englishtofrench(0), "Bonjour")

    def test_frenchtoenglish(self):
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchtoenglish(0), "Hello")

if __name__ == '__main__':
    unittest.main()