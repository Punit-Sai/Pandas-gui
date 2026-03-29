import tkinter as tk

def greet_user():
    username = entry.get()  
    greeting_label.config(text=f"Hello {username}!")
root = tk.Tk()
root.title("Hello User App")
root.geometry("300x150")
tk.Label(root, text="Enter your name:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
tk.Button(root, text="Say Hello", command=greet_user).pack(pady=5)
greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=5)
root.mainloop()