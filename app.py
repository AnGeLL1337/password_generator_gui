import pyperclip  # To copy the password to the clipboard
from tkinter import * # To create the GUI 
from bs4 import BeautifulSoup  # To parse the xml file

from password_generator import generate_password

# Variables
font_size: int  # To store the font size
font_family: str  # To store the font family
bool_dark_theme: bool  # To check if the default theme is dark or light

# To read the xml file
with open("config.xml") as f:
    soup = BeautifulSoup(f, "xml")

bool_dark_theme = (
    False if soup.default_theme.text == "dark" else True
)  # To check if the default theme is dark or light

dark_theme = soup.dark_theme  # To get the dark theme
dark_colors = [
    color.text for color in dark_theme.find_all("color")
]  # To get the colors of the dark theme

light_theme = soup.light_theme  # To get the light theme
light_colors = [
    color.text for color in light_theme.find_all("color")
]  # To get the colors of the light theme

font_size = int(soup.font_size.text)  # To get the font size
font_family = soup.font_family.text  # To get the font family

# Color Palette
dark_theme, dark_theme_active, dark_theme_font = dark_colors  # To unpack the list
light_theme, light_theme_active, light_theme_font = light_colors  # To unpack the list






# App Window
root = Tk()  # To create the window
root.geometry("500x250")  # To set the size of the window
root.title("Password Generator")  # To change the title of the window
root.resizable(0, 0)  # To prevent resizing the window

# Variables
bool_numbers = (
    BooleanVar()
)  # To check if the user wants to include numbers in the password
bool_symbols = (
    BooleanVar()
)  # To check if the user wants to include symbols in the password


# Widgets
pass_label = Label(root, text="Password", font=(font_family, font_size))
pass_label.grid(row=0, column=1)
pass_text = Text(
    root,
    font=("Times New Roman Bold", font_size + 2),
    state=DISABLED,
    width=25,
    height=2,
)
# To create text widget invisible
pass_text.configure(
    bd=0,
    highlightthickness=0,
    bg=light_theme,
    fg="red",
    insertbackground=light_theme_font,
    cursor="arrow",
)
# To center text
pass_text.tag_configure("center", justify=CENTER)
pass_text.grid(row=1, column=1, pady=5)

# To change theme
change_theme_button = Button(
    root,
    text="Change Theme",
    font=(font_family, font_size),
    command=lambda: change_theme(),
)
change_theme_button.grid(row=0, column=2)

# "end-1c" because it includes a new line character
copy_button = Button(
    root,
    text="Copy",
    font=(font_family, font_size),
    command=lambda: pyperclip.copy(pass_text.get(1.0, "end-1c")),
)
copy_button.grid(row=1, column=2)


check_numbers = Checkbutton(
    text="Include Numbers",
    font=(font_family, font_size),
    variable=bool_numbers,
    onvalue=True,
    offvalue=False,
)
# To select the checkbutton by default
check_numbers.select()
check_numbers.grid(row=3, column=2)

check_symbols = Checkbutton(
    text="Include Symbols",
    font=(font_family, font_size),
    variable=bool_symbols,
    onvalue=True,
    offvalue=False,
)
# To select the checkbutton by default
check_symbols.select()
check_symbols.grid(row=4, column=2)


len_label = Label(root, text="Password Length", font=(font_family, font_size))
len_label.grid(row=2, column=1)
len_scale = Scale(root, from_=8, to_=32, orient=HORIZONTAL, length=300)
len_scale.config(
    bg=light_theme,
    fg=light_theme_font,
    troughcolor=light_theme_active,
    sliderrelief=FLAT,
    sliderlength=20,
    highlightthickness=0,
)
# To set the scale by default
len_scale.set(12)
len_scale.grid(row=3, column=1, padx=10)

# To generate password
generate_button = Button(
    root,
    text="Generate Password",
    font=(font_family, font_size),
    command=lambda: push_text(pass_text, generate_password()),
)
generate_button.grid(row=4, column=1, pady=5)

# Functions
def change_theme():
    """
    To change the theme of the app\n
    note: The theme is changed by changing the color of the widgets
    """
    global bool_dark_theme  # To change the value of the variable

    if not bool_dark_theme:  # If the theme is light
        root.config(bg=dark_theme)
        pass_label.config(bg=dark_theme, fg=dark_theme_font)
        pass_text.config(bg=dark_theme, insertbackground=dark_theme_font)
        change_theme_button.config(
            bg=dark_theme,
            fg=dark_theme_font,
            activebackground=dark_theme_active,
            activeforeground=dark_theme_font,
        )
        copy_button.config(
            bg=dark_theme,
            fg=dark_theme_font,
            activebackground=dark_theme_active,
            activeforeground=dark_theme_font,
        )
        check_numbers.config(
            bg=dark_theme,
            fg=dark_theme_font,
            activebackground=dark_theme,
            activeforeground=dark_theme_font,
            selectcolor=dark_theme,
        )
        check_symbols.config(
            bg=dark_theme,
            fg=dark_theme_font,
            activebackground=dark_theme,
            activeforeground=dark_theme_font,
            selectcolor=dark_theme,
        )
        len_label.config(bg=dark_theme, fg=dark_theme_font)
        len_scale.config(
            bg=dark_theme,
            fg=dark_theme_font,
            troughcolor=dark_theme_active,
            sliderrelief=FLAT,
            sliderlength=20,
            highlightthickness=0,
        )
        generate_button.config(
            bg=dark_theme,
            fg=dark_theme_font,
            activebackground=dark_theme_active,
            activeforeground=dark_theme_font,
        )
        bool_dark_theme = True
    else:  # If the theme is dark
        root.config(bg=light_theme)
        pass_label.config(bg=light_theme, fg=light_theme_font)
        pass_text.config(bg=light_theme, insertbackground=light_theme_font)
        change_theme_button.config(
            bg=light_theme,
            fg=light_theme_font,
            activebackground=light_theme_active,
            activeforeground=light_theme_font,
        )
        copy_button.config(
            bg=light_theme,
            fg=light_theme_font,
            activebackground=light_theme_active,
            activeforeground=light_theme_font,
        )
        check_numbers.config(
            bg=light_theme,
            fg=light_theme_font,
            activebackground=light_theme,
            activeforeground=light_theme_font,
            selectcolor=light_theme,
        )
        check_symbols.config(
            bg=light_theme,
            fg=light_theme_font,
            activebackground=light_theme,
            activeforeground=light_theme_font,
            selectcolor=light_theme,
        )
        len_label.config(bg=light_theme, fg=light_theme_font)
        len_scale.config(
            bg=light_theme,
            fg=light_theme_font,
            troughcolor=light_theme_active,
            sliderrelief=FLAT,
            sliderlength=20,
            highlightthickness=0,
        )
        generate_button.config(
            bg=light_theme,
            fg=light_theme_font,
            activebackground=light_theme_active,
            activeforeground=light_theme_font,
        )
        bool_dark_theme = False


def clear_text(text: Text):
    """
    @param text: The text widget to clear\n
    Clears the text in the text widget
    """
    text.configure(state=NORMAL)  # To make the text widget editable
    text.delete(1.0, END)  # END = 'end'
    text.configure(state=DISABLED)  # To make the text widget uneditable


def push_text(text: Text, text_to_push: str):
    """
    @param text: The text widget to push the text to\n
    @param text_to_push: The text to push to the text widget\n
    Pushes the text to the text widget
    """
    clear_text(text)
    text.configure(state=NORMAL)  # To make the text widget editable
    text.insert("1.0", text_to_push)
    text.configure(state=DISABLED)  # To make the text widget uneditable
    text.tag_add("center", "1.0", "end")
