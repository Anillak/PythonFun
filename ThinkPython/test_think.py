import unittest, math


from ThinkPython.think import *


class WordPlayTest(unittest.TestCase):

    def test_has_no_e(self):
        self.assertTrue(has_no_e("cat"))

    def test_has_e(self):
        self.assertFalse(has_no_e("e"))

    def test_avoids_when_word_not_containing(self):
        self.assertTrue(avoids("cat", "ebsqw"))

    def test_avoids_when_word_contains(self):
        self.assertFalse(avoids("cat", "bskafdj"))

    def test_uses_only_single_letter(self):
        self.assertTrue(uses_only("ooooo", "o"))

    def test_uses_only_correct_word(self):
        self.assertTrue(uses_only("orientation", "orientawpl"))

    def test_uses_only_word_uses_more(self):
        self.assertFalse(uses_only("orientation", "orientwpl"))

    def test_uses_all_single_letter(self):
        self.assertTrue(uses_all("ooooo", "o"))

    def test_uses_all_correct_word(self):
        self.assertTrue(uses_all("orientation", "orienta"))

    def test_uses_all_word_uses_not_all(self):
        self.assertFalse(uses_all("orientation", "orientawpl"))

    def test_uses_all_word_uses_more(self):
        self.assertFalse(uses_all("orientation", "orientwpl"))

    def test_is_abecedarian_single_letter(self):
        self.assertTrue(is_abecedarian("a"))

    def test_is_abecedarian_two_letters(self):
        self.assertTrue(is_abecedarian("ab"))
        self.assertFalse(is_abecedarian("ba"))

    def test_is_abecedarian_correct_words(self):
        self.assertTrue(is_abecedarian("abcdefg"))

    def test_is_abecedarian_wrong_words(self):
        self.assertFalse(is_abecedarian("sgadfgdf"))

class IterationTest(unittest.TestCase):

    def test_square_root(self):
        self.assertAlmostEqual(square_root(25, 10), math.sqrt(25))


class FruitfulFunctionsTest(unittest.TestCase):

    def test_ackermann_first(self):
        self.assertEqual(ack(0, 2), 3)

    def test_ackermann_second(self):
        self.assertEqual(ack(1, 0), 2)

    def test_ackermann_third(self):
        self.assertEqual(ack(1, 2), 4)
        self.assertEqual(ack(3, 4), 125)

    def test_is_palindrome_initial(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("noon"))
        self.assertTrue(is_palindrome("redivider"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("nothing"))
        self.assertFalse(is_palindrome("cat"))

    def test_is_power_base_case(self):
        self.assertTrue(is_power(0, 2))
        self.assertTrue(is_power(1, 2))

    def test_is_power(self):
        self.assertTrue(is_power(4, 2))
        self.assertTrue(is_power(27, 3))