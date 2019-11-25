import tkinter as tk

def message():
    print("Cerberus Online.")
    
    
root = tk.Tk();
frame = tk.Frame(root)
frame.pack()

onButton = tk.Button(frame, 
                   text="ON", 
                   fg="GREEN",
                   command=message)

onButton.pack(side=tk.LEFT)
offButton = tk.Button(frame, 
                   text="OFF", 
                   fg="red",
                   command=quit)
offButton.pack(side=tk.RIGHT)


root.mainloop()