import tkinter as tk

root = tk.Tk()
root.title("Geometry Demo")
root.geometry("300x200")

frame1 = tk.Frame(root)
frame1.pack()
tk.Label(frame1, text="Pack").pack()
tk.Button(frame1, text="Pack Button").pack()

frame2 = tk.Frame(root)
frame2.pack()
tk.Label(frame2, text="Grid").pack()
frame_grid = tk.Frame(frame2)
frame_grid.pack()
tk.Button(frame_grid, text="Grid Button").grid(row=0, column=0)

frame3 = tk.Frame(root, height=50)
frame3.pack()
tk.Label(frame3, text="Place").pack()
tk.Button(frame3, text="Place Button").place(x=50, y=20)

root.mainloop()