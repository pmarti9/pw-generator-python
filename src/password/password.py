import logging
import math
import random

from datastore.redis_config import RedisConfig

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('password')

class Password:

    def __init__(self, name):
        self.name = name

    def write_password(self):
        while True:
            try:
                characters = int(
                    input(f"how many characters do you want your password to be {self.name}? Pick a number between 8 and 20\n"))

                if characters < 8 or characters > 20:
                    log.info("please pick a number between 8 and 20")

                else:

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
            except ValueError:
                log.info("please enter an integer between 8 and 20 and not a character or symbol")
                continue

    def save_password_to_redis_store(self, password):
        r = RedisConfig(host='localhost', port=6379, db=0)
        redis_connection = r.get_redis_connection()
        redis_connection.set(self.name, password)
