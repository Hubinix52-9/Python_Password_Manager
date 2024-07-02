import secrets
import string


class password_security:
    def __password_salting():
        pass

    def __generate_salt(salt_length=24):
        """
        Generate a random salt of specified length.

        Parameters:
        salt_length (int): The length of the salt to be generated.
        Default is 24.

        Returns:
        str: A random salt of specified length.

        The salt is generated using a combination of ASCII letters,
        digits, and punctuation.
        """
        keyboard_characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )
        secure_salt = ''.join(
            secrets.choice(keyboard_characters) for _ in range(salt_length))
        return secure_salt

    def