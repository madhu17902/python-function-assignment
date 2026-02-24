def count_vowels(text):
    v = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in v:
            count += 1
    return count

s = input("Enter string: ")
print("Vowels:", count_vowels(s))
