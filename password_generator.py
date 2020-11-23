import random
import os
import sys
import argparse

def get_upper_and_lower_case(letters):
    all_letters = [char.upper() for char in letters]
    all_letters.extend([char.lower() for char in letters])
    return all_letters

def get_user_combination(password_size):
    letters_in_combination = int(args.letters)
    numbers_in_combination = int(args.numbers)
    special_chars_in_combination = int(args.specialchars)
    
    return (letters_in_combination, numbers_in_combination, special_chars_in_combination)

def autogenerate_combination(password_size):
    max_num_and_spl_chars = int(0.25 * password_size)
    max_letters = password_size - int((2 * max_num_and_spl_chars))
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

def validate_password_size(password_size):
    if not (8 <= password_size <= 256):
        print("The password size provided doesn't satisfy the limits. Please try again")
        exit()

def exit():
    sys.exit()

# Main program starts here

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="Generate a customizable alphanumeric password",
    epilog="\n\nExamples:"\
           "\n> python password_generator.py" \
           "\ng.KlZ0-zr21_"
           "\n\n> python password_generator.py --size 16" \
           "\nDX5im&3hr*7s%q;4"
           "\n\n> python password_generator.py --letters 13 --numbers 1 --specialchars 1" \
           "\nFLtyKqR:sbU8BTH")

parser.add_argument("--size",
                    metavar="size",
                    type=int,
                    help="set password size between 8 to 256 characters, default size is 12 characters")

parser.add_argument("--letters",
                    metavar="letters",
                    type=int,
                    help="override size and set number of letters to be included in your custom password")

parser.add_argument("--numbers",
                    metavar="numbers",
                    type=int,
                    help="override size and set number of digits to be included in your custom password")

parser.add_argument("--specialchars",
                    metavar="specialchars",
                    type=int,
                    help="override size and set number of special characters to be included in your custom password")

args = parser.parse_args()

# all upper and lower case alphabets as a list
alphabet = get_upper_and_lower_case("abcdefghijklmnopqrstuvwxyz")

# all digits and special characters as a list
numbers = [num for num in '0123456789']
special_chars = [char for char in '!?@#$%&\()[]{<>}/*+-=:;,.`~_|']

# randomise the lists to prevent patterns in passwords generated
for list in [alphabet, numbers, special_chars]:
    random.shuffle(list)

# save password as a list for easy shuffling using random module
password_characters = []

express_settings = False
user_combination = False
password_size = 0
letters_in_combination = numbers_in_combination = special_chars_in_combination = 0

if len(sys.argv) < 2:
    password_size = 12
    express_settings = True
elif args.size:
    password_size = args.size
elif args.letters or args.numbers or args.specialchars:
    if not args.letters:
        args.letters = 0
    if not args.numbers:
        args.numbers = 0
    if not args.specialchars:
        args.specialchars = 0
    password_size = sum([args.letters, args.numbers, args.specialchars])
    user_combination = True

if not express_settings:
    validate_password_size(password_size)

if user_combination:
    letters_in_combination = args.letters
    numbers_in_combination = args.numbers
    special_chars_in_combination = args.specialchars
else:
    letters_in_combination, numbers_in_combination, special_chars_in_combination = autogenerate_combination(password_size)

if express_settings:
    password_characters.extend(alphabet[0:letters_in_combination])
    password_characters.extend(numbers[0:numbers_in_combination])
    password_characters.extend(special_chars[0:special_chars_in_combination])
else:
    if letters_in_combination > 0:
        password_characters.extend(generate_password(alphabet, letters_in_combination))

    if numbers_in_combination > 0:
        password_characters.extend(generate_password(numbers, numbers_in_combination))

    if special_chars_in_combination > 0:
        password_characters.extend(generate_password(special_chars, special_chars_in_combination))

random.shuffle(password_characters)
password = "".join(password_characters)
print(password)