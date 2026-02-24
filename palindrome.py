def check_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

word = input("Enter word: ")
print(check_palindrome(word))
