import math
import random


def write_password():
    characters = int(input("how many characters do you want your password to be? Pick a number between 8 and 20"))

    if characters < 8 or characters > 20:
        return "please pick a number between 8 and 20"

    lowercase = ["abcdefghijklmnopqrstuvwxyz"]
    uppercase = ["abcdefghijklmnopqrstuvwxyz".upper()]
    numbers = ["1234567890"]
    special = ["!@#$%^&*()?<>,./"]

    selected_criteria = [*lowercase, *uppercase, *special, *numbers]

    final_criteria = selected_criteria[0] + selected_criteria[1] + selected_criteria[2] + selected_criteria[3]

    pw_string = ""
    for i in range(characters):
        pw_string += final_criteria[math.floor(random.random() * len(final_criteria))]

    return pw_string


if __name__ == "__main__":
    print("hello....")
    password = write_password()
    print(password)
