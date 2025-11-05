import random
import string

def generate_otp(length=6)-> str:
    """ Function to generate otp number """
    return "".join(random.choices(string.digits, k=length))