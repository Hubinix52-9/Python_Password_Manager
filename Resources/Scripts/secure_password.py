import string
import os
import bcrypt


class password_security:
    def __get_pep_value(self) -> string:
        pepper = os.environ.get('pm_pep')
        return pepper

    def hash_password(self, passw: string):
        salt = bcrypt.gensalt(12)
        pepper = self.__get_pep_value()
        try:
            peppered_password = pepper + passw
        except TypeError:
            print("Environment variable pm_pep is not set")
        else:
            encoded_password = peppered_password.encode()
            hashed_password = bcrypt.hashpw(encoded_password, salt)
            return hashed_password

