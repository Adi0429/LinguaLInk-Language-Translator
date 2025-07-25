from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

# Initialize the main window
root = Tk()
root.title("LinguaLink")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="white")

# Function to update the label text based on combobox selection
def update_labels():
    label1.configure(text=combo1.get().upper())
    label2.configure(text=combo2.get().upper())

# Translation function
def translate_now():
    text_to_translate = text1.get(1.0, END)
    if text_to_translate.strip():  # Ensure there is text to translate
        try:
            translator = Translator()
            translated = translator.translate(text_to_translate, src=combo1.get(), dest=combo2.get())
            text2.delete(1.0, END)
            text2.insert(END, translated.text)
        except Exception as e:
            messagebox.showerror("Translation Error", f"An error occurred: {e}")
    else:
        messagebox.showinfo("Input Required", "Please enter text to translate.")

# Icon for the application
try:
    image_icon = PhotoImage(file="lingual.png")
    root.iconphoto(False, image_icon)
except:
    messagebox.showwarning("Icon Missing", "Icon file 'lingual.jpeg' not found.")

# Arrow image for visual separator
try:
    arrow_image = PhotoImage(file="arrow.png")
    Label(root, image=arrow_image, width=150, bg="white").place(x=460, y=50)
except:
    pass

# Get the languages supported by Google Translate
languages = googletrans.LANGUAGES
language_values = list(languages.values())
language_keys = list(languages.keys())

# Source language combobox
combo1 = ttk.Combobox(root, values=language_values, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("english")
combo1.bind("<<ComboboxSelected>>", lambda e: update_labels())

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Destination language combobox
combo2 = ttk.Combobox(root, values=language_values, font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("select language")
combo2.bind("<<ComboboxSelected>>", lambda e: update_labels())

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# First frame for input text
frame1 = Frame(root, bg="black", bd=5)
frame1.place(x=10, y=118, width=440, height=210)

text1 = Text(frame1, font="Roboto 16", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(frame1, command=text1.yview)
scrollbar1.pack(side="right", fill='y')
text1.configure(yscrollcommand=scrollbar1.set)

# Second frame for translated text
frame2 = Frame(root, bg="black", bd=5)
frame2.place(x=620, y=118, width=440, height=210)

text2 = Text(frame2, font="Roboto 16", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(frame2, command=text2.yview)
scrollbar2.pack(side="right", fill='y')
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate_button = Button(root, text="Translate", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1, 
                          width=10, height=2, bg="black", fg="white", command=translate_now)
translate_button.place(x=476, y=250)

# Initialize the label update function
update_labels()

root.mainloop()
