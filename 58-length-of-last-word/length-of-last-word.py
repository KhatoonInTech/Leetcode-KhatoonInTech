class Solution:
    def lengthOfLastWord(self, s: str) -> int:

    # Remove leading and trailing whitespace using strip()
         stripped_string = s.strip()

    # Check if the stripped string is empty (no characters)
         if not stripped_string:
              return 0

    # Check if all characters are alphabets or spaces using any() and isalpha()/isspace()
         if not all(char.isalpha() or char.isspace() for char in stripped_string):
              return "Enter valid input"

    # Split the string into words using split()
         words = stripped_string.split()
  # Check if there are any words after splitting (handles single whitespace characters)         
         if not words:
              return 0

    # Get the last word and return its length
         last_word = words[-1]
         return len(last_word)

# Example usage
solution = Solution()
result = solution.lengthOfLastWord("Hello, world!")
print(result)  # Output: 5 (length of "world!")
