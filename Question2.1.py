#A]
def count_unique_consonants(string):
  string = string.lower()
  vowels = {'a', 'e', 'i', 'o', 'u'}
  consonants = set()
  for char in string:
    if char not in vowels and char not in consonants:
      consonants.add(char)
  return len(consonants)

print(count_unique_consonants("cat")) #2
print(count_unique_consonants("cataract")) #3
print(count_unique_consonants("elephant")) #5
print(count_unique_consonants("aeiou")) #0

#B]
# The function converts the string to lower case, which takes O(n) time and O(n) space.
# The function defines a set of vowels, which takes O(1) time and O(1) space.
# The function initializes an empty set to store the consonants, which takes O(1) time and O(1) space.
# The function loops through each character in the string, which takes O(n) time.
# For each character, it checks if it is not a vowel and not already in the consonants set, which takes O(1) time.
# It adds it to the consonants set, which takes O(1) time and O(1) space.
# Therefore, the loop takes O(n) time and O(m) space in total.
# The function returns the size of the consonants set, which takes O(1) time and O(1) space.
# The overall time complexity of the function is O(n).