import logging

from password.password import Password

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger('main')


    log.info("Hello, and welcome to the password generator!\n")
    log.info("Please enter your name below to get started\n")
    name = input("Name: ")
    p = Password(name)
    password = p.write_password()
    print(password)
