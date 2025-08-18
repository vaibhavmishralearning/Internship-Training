print("\n__Check Vowel or Consonant______________________\n")
character = input('Enter Any Character : ').lower().strip()

# if (character in "aeiou"):
if (character == 'a' or character == 'e' or character == 'i' or character == 'u'):
    print("\nOUTPUT:\nThe Entered Character is a Vowel\n")
else:
    print("\nOUTPUT:\nThe Entered Character is a Consonant\n")