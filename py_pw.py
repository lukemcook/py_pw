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
# shuffle character list, create empty pw list
random.shuffle(character_list)
pw = []
# add variable for tracking attempts
attempts = 0
# loop and try/except for error handling
while True:
    try:
        pw_length = int(input("Enter desired password length, e.g. 12 for 12 characters and be at least 5: "))
        if pw_length <= 4:
            raise ValueError
# loop to match desired password length
        for char in range(pw_length):
            pw.append(random.choice(character_list))
        print(f"Your generated password is: {''.join(pw)}")
# pyperclip copies password to clipboard
        pyperclip.copy(''.join(pw))
        print(f"Copied {''.join(pw)} to clipboard")
        break
# except catches input error and updates failed attempts
    except ValueError:
        attempts += 1
        if attempts >= 3:
            print("Exiting due to 3 incorrect attempts.")
            break
        print("Password should contain only whole numbers and contain 5 or more characters.")
