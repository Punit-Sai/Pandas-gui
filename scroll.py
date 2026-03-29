import tkinter as tk
from tkinter import messagebox, filedialog

def calc():
    try:
        result = eval(entry.get())
        listbox.insert(tk.END, f"{entry.get()} = {result}")
        entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error","Invalid Expression")

def save():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file,"w") as f:
            for i in listbox.get(0, tk.END):
                f.write(i+"\n")
        messagebox.showinfo("Saved","History saved!")

root = tk.Tk()
root.title("Mini Calculator")
entry = tk.Entry(root); entry.pack()
tk.Button(root,text="Calculate",command=calc).pack()
frame = tk.Frame(root); frame.pack()
scroll = tk.Scrollbar(frame); scroll.pack(side=tk.RIGHT,fill=tk.Y)
listbox = tk.Listbox(frame, yscrollcommand=scroll.set, width=30, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH); scroll.config(command=listbox.yview)

menu = tk.Menu(root); root.config(menu=menu)
file_menu = tk.Menu(menu,tearoff=0); menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Save History",command=save); file_menu.add_command(label="Exit",command=root.quit)

root.mainloop()