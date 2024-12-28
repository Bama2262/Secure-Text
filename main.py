from tkinter import *
from tkinter import messagebox
import base64

def encrypt():
    password = code.get()
    message = text_input.get(1.0, END).strip()

    if not message:
        messagebox.showerror("Error", "Enter the text to encrypt")
        return

    if password == "1234":
        encoded_message = message.encode("ascii")
        encrypted_bytes = base64.b64encode(encoded_message)
        encrypted = encrypted_bytes.decode("ascii")
        display_result("ENCRYPTION", encrypted, "#ed3833")
    elif password == "":
        messagebox.showerror("Error", "Enter the password")
    else:
        messagebox.showerror("Error", "Invalid password")

def decrypt():
    password = code.get()
    message = text_input.get(1.0, END).strip()

    if not message:
        messagebox.showerror("Error", "Enter the text to decrypt")
        return

    if password == "1234":
        encoded_message = message.encode("ascii")
        try:
            decrypted_bytes = base64.b64decode(encoded_message)
            decrypted = decrypted_bytes.decode("ascii")
            display_result("DECRYPTION", decrypted, "#00bd56")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during decryption: {e}")
    elif password == "":
        messagebox.showerror("Error", "Enter the password")
    else:
        messagebox.showerror("Error", "Invalid password")

def display_result(title, result, color):
    result_screen = Toplevel(screen)
    result_screen.title(title)
    result_screen.geometry("400x200")
    result_screen.configure(bg=color)

    Label(result_screen, text=title, font="arial", fg="white", bg=color).place(x=10, y=0)
    output_text = Text(result_screen, font="Arial 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    output_text.place(x=10, y=40, width=380, height=150)
    output_text.insert(END, result)

def reset():
    code.set("")
    text_input.delete(1.0, END)

def main_screen():
    global screen
    global code
    global text_input
    screen = Tk()
    screen.geometry("375x398")
    screen.title("Encryption and Decryption Program")

    Label(screen, text="Enter the text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text_input = Text(screen, font="Arial 13", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text_input.place(x=10, y=50, width=355, height=100)

    Label(screen, text="Enter the password (1234)", fg="black", font=("calibri", 13)).place(x=15, y=170)
    code = StringVar()
    Entry(screen, textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=15, y=200)

    Button(screen, text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="black", bd=0, command=encrypt).place(x=10, y=250)
    Button(screen, text="DECRYPT", height="2", width=23, bg="#00bd56", fg="black", bd=0, command=decrypt).place(x=200, y=250)
    Button(screen, text="RESET PROGRAM", height="2", width=50, bg="#1089ff", fg="black", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()