import tkinter as tk

FONT = ("Arial", 12, "bold")


def button_clicked():
    new_text = int(user_input.get()) * 1.60934
    print(new_text)
    km_input_label.configure(text=f"{new_text:.2f}")


# Window
window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
user_input = tk.Entry(width=6, font=FONT)
user_input.grid(column=1, row=0)

# Labels
label_1 = tk.Label(text="Miles", font=FONT)
label_1.grid(column=2, row=0)

label_2 = tk.Label(text="is equal to", font=FONT)
label_2.grid(column=0, row=1)

km_input_label = tk.Label(font=FONT)
km_input_label.grid(column=1, row=1)

label_3 = tk.Label(text="Km", font=FONT)
label_3.grid(column=2, row=1)

# Button
button = tk.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
