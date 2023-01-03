import unittest
from translator import english_to_french, french_to_english

class Testingenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Thank you'), 'Merci')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        
class Testingfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Merci'), 'Thank you')
        self.assertEqual(french_to_english('Au revoir'), 'Good bye')