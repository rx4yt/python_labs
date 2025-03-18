#WAP to accept a string and count the frequency of each vowel.


def count_vowel_frequency(s):
    vowels = "aeiouAEIOU"
    frequency = {v: 0 for v in vowels}

    for char in s:
        if char in frequency:
            frequency[char] += 1

   
    frequency = {k: v for k, v in frequency.items() if v > 0}
    return frequency


input_str = input("Enter a string: ")
vowel_count = count_vowel_frequency(input_str)

print("Vowel frequencies:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")
