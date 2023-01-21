import secrets  # To generate secure random passwords
import string  # To get the ascii letters and digits
import app
from tkinter import *  # To create the GUI


# Functions
def generate_password():
    """
    Generates a random password
    """

    password = ""
    punctuation = "!@#$%^&*"  # I don't want to include all the symbols because some of them don't work in some websites
    alphabet = (
        string.ascii_letters
        + (string.digits if app.bool_numbers.get() else "")
        + (punctuation if app.bool_symbols.get() else "")
    )
    for _ in range(app.len_scale.get()):
        password += secrets.choice(alphabet)

    return password
