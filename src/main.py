import logging

from password.password import Password

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('main')

if __name__ == "__main__":
    log.info("Hello, and welcome to the password generator!\n")
    log.info("Please enter your name below to get started\n")
    name = input("Name: ")
    p = Password(name)
    password = p.write_password()
    p.save_password_to_redis_store(password)
    print(password)
