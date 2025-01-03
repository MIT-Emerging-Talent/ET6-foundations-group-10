import unittest
from solutions.is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Test the is_palindrome function."""

    def test_empty_string(self):
        """It should return True for an empty string."""
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """It should return True for single character strings."""
        self.assertTrue(is_palindrome("a"))

    def test_level_palindrome(self):
        """It should return True for the palindrome 'level'."""
        self.assertTrue(is_palindrome("level"))

    def test_radar_palindrome(self):
        """It should return True for the palindrome 'radar'."""
        self.assertTrue(is_palindrome("radar"))

    def test_hello_is_not_palindrome(self):
        """It should return False for the non-palindrome 'hello'."""
        self.assertFalse(is_palindrome("hello"))

    def test_world_is_not_palindrome(self):
        """It should return False for the non-palindrome 'world'."""
        self.assertFalse(is_palindrome("world"))

    def test_mixed_case_palindromes_return_true(self):
        """It should return True for palindromes with mixed lower-case and upper-case characters."""
        self.assertTrue(is_palindrome("RaceCar"))

    def test_palindromes_with_spaces_return_true(self):
        """It should return True for palindromes with spaces and mixed cases."""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_palindrome_with_numbers_returns_true(self):
        """It should return True for palindromes containing numbers."""
        self.assertTrue(is_palindrome("12321"))

    def test_non_palindrome_numbers_return_false(self):
        """It should return False for non-palindrome numbers."""
        self.assertFalse(is_palindrome("12345"))

    def test_palindrome_with_special_characters_returns_true(self):
        """It should return True for palindromes with special characters."""
        self.assertTrue(is_palindrome("!@#$%^&*()_+_)(*&^%$#@!"))

    def test_non_palindrome_with_special_characters_returns_false(self):
        """It should return False for non-palindromes with special characters."""
        self.assertFalse(is_palindrome("hello!"))


if __name__ == "__main__":
    unittest.main()
