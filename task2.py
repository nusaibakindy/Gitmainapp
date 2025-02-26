num_of_vowels = input("Vowel counter: Write a sentence: ")
all_vowels = "aeiouAEIOU"
vowels_count = 0

for char in num_of_vowels:
    if char in all_vowels:
        vowels_count += 1

while not num_of_vowels:
    print("You entered an empty string. Please enter a valid string.")
    num_of_vowels = input("Vowel counter: Write a sentence: ")


print(f"The number of vowels in '{num_of_vowels}' is {vowels_count}")