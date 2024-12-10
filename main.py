import math
import random


class Password:
    def __init__(self, name):
        self.name = name

    def write_password(self):
        while True:
            pw_string = ""
            characters = int(
                input(f"how many characters do you want your password to be {self.name}? Pick a number between 8 and 20\n"))

            if characters < 8 or characters > 20:
                print("please pick a number between 8 and 20")
            else:

                lowercase = ["abcdefghijklmnopqrstuvwxyz"]
                uppercase = ["abcdefghijklmnopqrstuvwxyz".upper()]
                numbers = ["1234567890"]
                special = ["!@#$%^&*()?<>,./"]


                selected_criteria = [*lowercase, *uppercase, *special, *numbers]

                final_criteria = selected_criteria[0] + selected_criteria[1] + selected_criteria[2] + selected_criteria[3]

                for i in range(characters):
                    pw_string += final_criteria[math.floor(random.random() * len(final_criteria))]

                return pw_string
    


if __name__ == "__main__":
    p = Password("parker")
    password = p.write_password()
    print(password)
