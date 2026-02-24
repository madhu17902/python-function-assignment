def count_words(s):
    words = s.split()
    return len(words)

sentence = input("Enter sentence: ")
print("Word count:", count_words(sentence))
