from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import pyttsx3

# Initialize the main window
root = Tk()
root.title("LinguaLink - Your Smart Translator")
root.geometry("1080x480")
root.resizable(False, False)
root.configure(background="#e6f7ff")  # Softer background color

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to configure the TTS engine
def configure_tts_engine():
    try:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 120)
        engine.setProperty('volume', 1.0)
    except Exception as e:
        messagebox.showerror("TTS Configuration Error", f"An error occurred while configuring the TTS engine: {e}")

# Function to speak the translated text
def speak_text():
    text = text2.get(1.0, END).strip()
    if text:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Speech Error", f"An error occurred while reading the text: {e}")
    else:
        messagebox.showinfo("No Text", "There is no text to read.")

# Function to update the label text based on combobox selection
def update_labels():
    label1.configure(text=combo1.get().upper())
    label2.configure(text=combo2.get().upper())

# Translation function
def translate_now():
    text_to_translate = text1.get(1.0, END)
    if text_to_translate.strip():
        try:
            translator = Translator()
            translated = translator.translate(text_to_translate, src=combo1.get(), dest=combo2.get())
            text2.delete(1.0, END)
            text2.insert(END, translated.text)
        except Exception as e:
            messagebox.showerror("Translation Error", f"An error occurred: {e}")
    else:
        messagebox.showinfo("Input Required", "Please enter text to translate.")



# Copy translated text to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(text2.get(1.0, END).strip())
    messagebox.showinfo("Copied", "Translated text copied to clipboard!")

# Header
header = Frame(root, bg="#003366", height=70)
header.pack(fill=X)
Label(header, text="LinguaLink", font=("Poppins", 24, "bold"), fg="white", bg="#003366").pack(pady=10)
Label(header, text="Translate text instantly between multiple languages", font=("Poppins", 12), fg="#d9d9d9", bg="#003366").pack()

languages = LANGUAGES
language_values = list(languages.values())

# Source language combobox
combo1 = ttk.Combobox(root, values=language_values, font="Poppins 14", state="readonly")
combo1.place(x=110, y=90)
combo1.set("english")
combo1.bind("<<ComboboxSelected>>", lambda e: update_labels())

label1 = Label(root, text="ENGLISH", font="Poppins 18 bold", bg="white", fg="#333", width=18, bd=5, relief=GROOVE)
label1.place(x=90, y=130)

# Destination language combobox
combo2 = ttk.Combobox(root, values=language_values, font="Poppins 14", state="readonly")
combo2.place(x=730, y=90)
combo2.set("select language")
combo2.bind("<<ComboboxSelected>>", lambda e: update_labels())

label2 = Label(root, text="ENGLISH", font="Poppins 18 bold", bg="white", fg="#333", width=18, bd=5, relief=GROOVE)
label2.place(x=700, y=130)

# Input text frame
frame1 = Frame(root, bg="#333", bd=5)
frame1.place(x=10, y=200, width=440, height=210)
text1 = Text(frame1, font="Poppins 14", bg="white", fg="#333", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)
scrollbar1 = Scrollbar(frame1, command=text1.yview)
scrollbar1.pack(side="right", fill='y')
text1.configure(yscrollcommand=scrollbar1.set)

# Output text frame
frame2 = Frame(root, bg="#333", bd=5)
frame2.place(x=620, y=200, width=440, height=210)
text2 = Text(frame2, font="Poppins 14", bg="white", fg="#333", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)
scrollbar2 = Scrollbar(frame2, command=text2.yview)
scrollbar2.pack(side="right", fill='y')
text2.configure(yscrollcommand=scrollbar2.set)

# Buttons
btn_style = {"font": ("Poppins", 14), "width": 10, "height": 2, "bd": 1, "cursor": "hand2"}
Button(root, text="Translate", bg="#007bff", fg="white", command=translate_now, **btn_style).place(x=476, y=240)
Button(root, text="Copy", bg="#28a745", fg="white", command=copy_to_clipboard, **btn_style).place(x=476, y=300)
Button(root, text="Speak", bg="#ffc107", fg="black", command=speak_text, **btn_style).place(x=476, y=360)

# Footer
footer = Frame(root, bg="#003366", height=30)
footer.pack(side=BOTTOM, fill=X)
Label(footer, text="LinguaLink v1.0 | © 2024", font=("Poppins", 10), fg="#d9d9d9", bg="#003366").pack()

update_labels()
configure_tts_engine()
root.mainloop()
