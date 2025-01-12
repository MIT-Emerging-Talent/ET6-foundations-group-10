def is_anagram(words):
    """
    Check if two words in a string are anagrams of each other.
    
    Args:
        words (str): Two words separated by a comma (e.g., "listen,silent").
        
    Returns:
        bool: True if the words are anagrams, False otherwise.
    
    Examples:
        >>> is_anagram("listen,silent")
        True
        >>> is_anagram("play,yellow")
        False
        >>> is_anagram("earth,heart")
        True
        >>> is_anagram("read,ride")
        False
    """
    # Split the words using the comma
    word1, word2 = words.split(",")
    
    # Check if sorted characters of both words are the same
    return sorted(word1.strip()) == sorted(word2.strip())
