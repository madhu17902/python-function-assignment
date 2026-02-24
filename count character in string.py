def count_chars(s):
    count = 0
    for i in s:
        count += 1
    return count

text = input("Enter text: ")
print("Length:", count_chars(text))
