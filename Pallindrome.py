
# palindrome function
def palindrome(string):

    string = string.replace(" ","").lower()

    reverse_string = string[::-1]

    if string == reverse_string:
        return "It is a palindrome"

    else:
        return "Not a palindrome"


# main function
user_input = input("Enter a string: ")
check = palindrome(user_input)
print(check)