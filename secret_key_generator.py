import random
import string


def generate_secret_key():
    """Generate a random 50 character string for Django's SECRET_KEY"""

    return "".join(
        random.SystemRandom().choice(
            string.ascii_letters + string.digits + string.punctuation
        )
        for _ in range(50)
    )


if __name__ == "__main__":
    print(generate_secret_key())
