import random

def upper_and_lower_case_alphabets(letters):
    all_letters = [char.upper() for char in letters]
    all_letters.extend([char.lower() for char in letters])
    return all_letters

def identify_password_combination(password_size):
    # unpack tuple
    letters_in_combination, numbers_in_combination, special_chars_in_combination = autogenerate_combination(password_size)

    password_combination = input("Enter custom to customise your password combination OR" \
                                 "\nPress Enter to continue with suggested combination (default): ")
    if password_combination.lower() == "custom":
        letters_in_combination = int(input("Enter the number of letters: "))
        numbers_in_combination = int(input("Enter the number of numbers: "))
        special_chars_in_combination = int(input("Enter the number of special characters: "))
    
    return (letters_in_combination, numbers_in_combination, special_chars_in_combination)

def autogenerate_combination(password_size):
    max_num_and_spl_chars = int(0.25 * password_size)
    max_letters = password_size - int((2 * max_num_and_spl_chars))
    print(f"\nThe default password combination includes {int(max_letters)} alphabets, " \
           f"{(max_num_and_spl_chars)} numbers and {(max_num_and_spl_chars)} special characters")
    return (max_letters, max_num_and_spl_chars, max_num_and_spl_chars)

def generate_password(char_list, total_chars):
    exceeding_char_count = 0
    password_characters = []
    while exceeding_char_count >= 0:
        exceeding_char_count = total_chars - len(char_list)
        if total_chars > len(char_list):
            total_chars = len(char_list)
            password_characters.extend(char_list[0:total_chars])
            total_chars = exceeding_char_count
        else:
            password_characters.extend(char_list[0:total_chars])
            break
    
    return password_characters

# Main program starts here
# all upper and lower case alphabets as a list
alphabets = upper_and_lower_case_alphabets("abcdefghijklmnopqrstuvwxyz")

# all digits and special characters as a list
numbers = [num for num in '0123456789']
special_chars = [char for char in '!?@#$%&\()[]{<>}/*+-=:;,.`~_|']

# randomise the lists to prevent patterns in passwords generated
for list in [alphabets, numbers, special_chars]:
    random.shuffle(list)

# save password as a list for easy shuffling using random module
password_characters = []

# default password size

print("***MINIMAL PASS - PASSWORD GENERATOR TOOL***\n")
use_express_mode = input("Two modes available for generating password - express and custom" \
                         "\nEnter mode name OR" \
                         "\nPress Enter to continue with express (default): ")

if use_express_mode.lower() == "express" or len(use_express_mode) == 0:
    letters_in_combination, numbers_in_combination, special_chars_in_combination = autogenerate_combination(password_size=12)
    password_characters.extend(alphabets[0:letters_in_combination])
    password_characters.extend(numbers[0:numbers_in_combination])
    password_characters.extend(special_chars[0:special_chars_in_combination])
elif use_express_mode.lower() == "custom":
    while True:
        try:
            password_size = int(input("Enter the size of password (min:8, max: 256): "))
            if 8 <= password_size <= 256:
                break
            else:
                print("The password size provided doesn't satisfy the requirements. Please try again")
        except ValueError:
            print("Invalid password size, please enter numeric value")

    total_letters, total_numbers, total_special_chars = identify_password_combination(password_size)

    if total_letters > 0:
        password_characters.extend(generate_password(alphabets, total_letters))

    if total_numbers > 0:
        password_characters.extend(generate_password(numbers, total_numbers))

    if total_special_chars > 0:
        password_characters.extend(generate_password(special_chars, total_special_chars))
else:
    print("Invalid mode. Please try again")

random.shuffle(password_characters)
password = "".join(password_characters)
print(password)
