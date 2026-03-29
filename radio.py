import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x250")

gender_var = tk.StringVar()
gender_var.set("None")
hobby_var = tk.IntVar()

def show_selection():
    gender = gender_var.get()
    hobby = "Coding" if hobby_var.get() else "None"
    result_label.config(text=f"Gender: {gender}\nHobby: {hobby}")

tk.Label(root, text="Select Gender:").pack()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Checkbutton(root, text="Coding", variable=hobby_var).pack(pady=10)
tk.Button(root, text="Submit", command=show_selection).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()