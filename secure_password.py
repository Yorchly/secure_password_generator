import random
import sys
from constants import CHARACTERS_TYPES


def build_prev_password():
    """
    Build a previous password with: one character, one digit and one punctuation. This method is used to ensure
    that final password have at least one of the element mentioned above.

    :return: (list) -- return three elements chosen pseudo-randomly from CHARACTERS_TYPES["characters"], \
    CHARACTERS_TYPES["digits"], CHARACTERS_TYPES["punctuations"]

    """
    password_choices = ["characters", "digits", "punctuations"]

    return [random.choice(CHARACTERS_TYPES.get(element)) for element in password_choices]


def generating_pseudo_random_pass(pass_length):
    """
    Generates a pseudo random pass.

    :param pass_length: Length of the pass that will be build.
    :type pass_length: int
    :return: (list) -- return a password, with pass_length - 3 (three elements put in the list by \
    'build_prev_password()') elements, build with elements chosen pseudo-randomly from CHARACTERS_TYPES["all"]

    """
    prev_password = build_prev_password()

    # Shuffle ensures that elements obtains from build_prev_password() are not in the last three positions.
    return random.shuffle([random.choice(CHARACTERS_TYPES.get("all")) for i in range(0, pass_length - 3)] +
                          prev_password)


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

    print("The password generated is: " + "".join(password))
