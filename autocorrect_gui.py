import tkinter as tk
from tkinter import ttk
from spellchecker import SpellChecker

languages = {
    "English": "en",
    "Spanish": "es",
    "German": "de",
    "French": "fr",
    "Portuguese": "pt"
}

def correct_word():
    word = word_entry.get().strip()
    lang_name = lang_dropdown.get()
    lang_code = languages.get(lang_name, "en")

    if not word:
        corrected_label.config(text="⚠ Please enter a word.")
        suggestion_label.config(text="")
        return

    try:
        spell = SpellChecker(language=lang_code)
        corrected = spell.correction(word)
        suggestions = spell.candidates(word)

        corrected_label.config(text=f"✅ Corrected: {corrected}")
        suggestion_label.config(
            text=f"💡 Suggestions: {', '.join(suggestions) if suggestions else 'No suggestions found'}"
        )
    except Exception as e:
        corrected_label.config(text="❌ Error occurred.")
        suggestion_label.config(text=f"{e}")

# ----- GUI -----
root = tk.Tk()
root.title("TextSure – Multilingual Autocorrect")
root.geometry("600x500")
root.configure(bg="#2e003e")
root.resizable(False, False)

# Fonts
font_heading = ("Segoe UI", 22, "bold")
font_normal = ("Segoe UI", 12)
font_result = ("Segoe UI", 13)

# Header
header = tk.Label(
    root, text="🌈 TextSure",
    font=font_heading,
    bg="#2e003e", fg="#00e0d5"
)
header.pack(pady=15)

# Card Frame
card = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge")
card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=360)

# Language
lang_label = tk.Label(card, text="🌐 Language", font=font_normal, bg="white", fg="#4f1271")
lang_label.pack(pady=(20, 5))

lang_dropdown = ttk.Combobox(card, values=list(languages.keys()), font=("Segoe UI", 11), width=20)
lang_dropdown.set("English")
lang_dropdown.pack()

# Word entry
word_label = tk.Label(card, text="✍️ Enter Word", font=font_normal, bg="white", fg="#4f1271")
word_label.pack(pady=(20, 5))

word_entry = tk.Entry(
    card,
    font=("Segoe UI", 13),
    width=28,
    bg="#4f1271",
    fg="white",
    insertbackground="white",
    bd=2,
    relief="flat",
    highlightthickness=2,
    highlightcolor="#00e0d5"
)
word_entry.pack()

# Button
check_btn = tk.Button(
    card, text="✔ Check",
    font=("Segoe UI", 12, "bold"),
    bg="#00bcd4", fg="white",
    relief="flat", padx=15, pady=5,
    command=correct_word
)
check_btn.pack(pady=20)

# Output
corrected_label = tk.Label(card, text="", font=font_result, fg="#00e676", bg="white", wraplength=400, justify="center")
corrected_label.pack(pady=5)

suggestion_label = tk.Label(card, text="", font=font_normal, fg="#2196f3", bg="white", wraplength=400, justify="center")
suggestion_label.pack()

# Footer
footer = tk.Label(root, text="🔹 Crafted with Color by You", font=("Segoe UI", 10), bg="#2e003e", fg="#b39ddb")
footer.pack(side="bottom", pady=10)

root.mainloop()
