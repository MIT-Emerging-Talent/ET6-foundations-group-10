import unittest
from is_palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    """Test the is_palindrome function."""
    
    def test_empty_string(self):
        """It should return True for an empty string."""
        self.assertTrue(is_palindrome(""))
    
    def test_single_character(self):
        """It should return True for single character strings."""
        self.assertTrue(is_palindrome("a"))
    
    def test_simple_palindrome(self):
        """It should return True for simple palindromes."""
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
    
    def test_non_palindrome(self):
        """It should return False for non-palindromes."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
    
    def test_mixed_case_palindrome(self):
        """It should handle mixed case palindromes."""
        self.assertTrue(is_palindrome("RaceCar"))
    
    def test_palindrome_with_spaces(self):
        """It should handle palindromes with spaces."""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
    
    def test_not_a_string(self):
        """It should raise AssertionError for non-string input."""
        with self.assertRaises(AssertionError):
            is_palindrome(12321)

if __name__ == "__main__":
    unittest.main()
    