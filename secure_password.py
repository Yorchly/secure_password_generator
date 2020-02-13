import random
import sys
from constants import CHARACTERS_LIST, DIGITS_LIST, PUNCTUATION_LIST, ALL


def build_prev_password():
    """
    Build a previous password with: one character, one digit and one punctuation. This method is used to ensure
    that final password have at least one of the element mentioned above.
    :return: type = list.
    """
    prev_password = []
    password_choices = ["characters", "digits", "punctuations"]

    while password_choices:
        choice = random.choice(password_choices)
        password_choices.pop(password_choices.index(choice))

        if choice == "characters":
            prev_password.append(random.choice(CHARACTERS_LIST))
        elif choice == "digits":
            prev_password.append(random.choice(DIGITS_LIST))
        elif choice == "punctuations":
            prev_password.append(random.choice(PUNCTUATION_LIST))

    return prev_password


def generating_pseudo_random_pass(pass_length):
    """
    Generates a pseudo random pass using the values in ALL constant.
    :param pass_length: type = int. Length of the pass that will be build.
    :return: type = list
    """
    prev_password = build_prev_password()

    return [random.choice(ALL) for i in range(0, pass_length - 3)] + prev_password


if __name__ == "__main__":
    length_of_pass = -1
    if len(sys.argv) > 2:
        sys.exit("Too many arguments! Only one required (length)")
    elif len(sys.argv) == 1:
        while length_of_pass < 8:
            length_of_pass = int(input("Introduce length of your password (8 minimum required, "
                                       "greater or equal than 15 recommended): "))
    else:
        length_of_pass = int(sys.argv[1]) if int(sys.argv[1]) > 8 else sys.exit("Length must be greater than 8")

    password = generating_pseudo_random_pass(length_of_pass)
    # Shuffle ensures that elements obtains from build_prev_password() are not in the top three positions.
    random.shuffle(password)
    print("The password generated is: " + "".join(password))
