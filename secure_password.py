import random


def read_from_file():
    file = open("characters", "r")
    characters_func = file.read().split(" ")
    return characters_func


def generating_random_pass(characters_func, length_of_pass_func):
    password_func = []
    for l in range(0, length_of_pass_func):
        password_func.append(random.choice(characters_func))

    return password_func


if __name__ == "__main__":
    characters = read_from_file()
    length_of_pass = -1
    while length_of_pass < 8:
        length_of_pass = int(input("Introduce length of your password (8 minimum required, "
                                   "greater or equal than 15 recommended): "))

    password = generating_random_pass(characters, length_of_pass)
    print("The password generated is: "+"".join(password))
