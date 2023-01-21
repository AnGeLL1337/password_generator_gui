import app  # To get the functions from the app.py file
from password_generator import *  # To get the functions from the password_generator.py file


def main():
    app.change_theme()  # To change the theme by default
    app.root.mainloop()  # To run the app


if __name__ == "__main__":
    main()
