import tkinter as tk
import os
window = tk.Tk()
window.title("Windows Power Controls")

def shutdown():
    return os.system('shutdown /s')
def restart():
    return os.system('shutdown /r')
shutdownbtn = tk.Button(
    window,
    text="Shutdown",
    command=shutdown
)
restartbtn = tk.Button(
    window,
    text="Restart",
    command=restart
)
shutdownbtn.grid(row=0, column=0, padx = 10, pady=10)
restartbtn.grid(row=0, column=1, padx = 10, pady=10)
window.mainloop()
