import random
import string
import pyperclip

# define characters for password creation
upper_case = list(string.ascii_uppercase)
lower_case = list(string.ascii_lowercase)
other = "@*&#%^()-+="
other = list(other)
digits = list(string.digits)
character_list = upper_case + lower_case + other + digits
# ask for password length and assign characters randomly
random.shuffle(character_list)
pw = []
pw_length = int(input("Enter desired password length, e.g. 12 for 12 characters: "))
# loop to adhere to desired password length
for char in range(pw_length):
    pw.append(random.choice(character_list))
print(f"Your generated password is: {''.join(pw)}")
# pyperclip copies password to clipboard
pyperclip.copy(''.join(pw))
print(f"Copied {''.join(pw)} to clipboard")
