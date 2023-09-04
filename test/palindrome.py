input_string = input()
input_string = input_string.replace(" ","").lower()
if input_string == input_string[::-1]:
    print("The string is an Palindrome")
else:
    print("The string is not an Palindrome")

