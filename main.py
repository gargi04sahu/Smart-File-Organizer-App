import tkinter as tk
from tkinter import messagebox, filedialog
from organizer import organize_downloads
import sys
import os

# ------------------ THEME STATE ------------------
is_dark = False
selected_folder = None

def browse_folder():
    global selected_folder
    folder = filedialog.askdirectory()
    if folder:
        selected_folder = folder
        folder_label.config(text=f"📁 Selected: {folder}")


# ------------------ ORGANIZE FUNCTION ------------------
def organize_files():
    if not selected_folder:
        messagebox.showwarning("No Folder Selected", "Please select a folder to organize.")
        return

    from organizer import organize_downloads
    moved, folders = organize_downloads(selected_folder)
    messagebox.showinfo("Done", f"✅ {moved} files organized into {folders} folders.")

# ------------------ THEME TOGGLE ------------------
def toggle_theme():
    global is_dark
    is_dark = not is_dark

    if is_dark:
        window.config(bg="#1e1e1e")
        header_label.config(bg="#1e1e1e", fg="#f5f5f5")
        organize_btn.config(bg="#2874f0", fg="white", activebackground="#1a5cb1")
        theme_toggle.config(text="☀ Light Mode", bg="#333", fg="white")
    else:
        window.config(bg="#f5f5f5")
        header_label.config(bg="#f5f5f5", fg="#1e1e1e")
        organize_btn.config(bg="#2874f0", fg="white", activebackground="#1558d6")
        theme_toggle.config(text="🌙 Dark Mode", bg="#e0e0e0", fg="black")

# ------------------ MAIN WINDOW ------------------
window = tk.Tk()
window.title("Smart File Organizer")
window.geometry("500x300")
window.config(bg="#f5f5f5")
window.resizable(False, False)

# Optional icon
if sys.platform.startswith("win"):
    try:
        window.iconbitmap("icon.ico")
    except:
        pass

# ------------------ THEME TOGGLE BUTTON (top-right) ------------------
theme_toggle = tk.Button(
    window,
    text="🌙 Dark Mode",
    font=("Segoe UI", 9, "bold"),
    command=toggle_theme,
    bg="#e0e0e0",
    fg="black",
    bd=0,
    relief="ridge",
    padx=10,
    pady=5
)
theme_toggle.place(x=380, y=10)

# ------------------ HEADER ------------------
header_label = tk.Label(
    window,
    text="📂 Welcome to Smart File Organizer",
    font=("Segoe UI", 16, "bold"),
    bg="#f5f5f5",
    fg="#1e1e1e"
)
header_label.pack(pady=60)

# Browse Folder Button
browse_btn = tk.Button(
    window,
    text="📁 Choose Folder",
    font=("Segoe UI", 10),
    command=browse_folder,
    bg="#d9d9d9",
    fg="black",
    bd=0,
    padx=10,
    pady=5
)
browse_btn.pack(pady=(10, 5))

# Folder path label
folder_label = tk.Label(
    window,
    text="📁 No folder selected",
    font=("Segoe UI", 9),
    bg=window["bg"],
    fg="#555"
)
folder_label.pack()


# ------------------ ORGANIZE BUTTON ------------------
organize_btn = tk.Button(
    window,
    text="⚡ Organize Now",
    font=("Segoe UI", 12, "bold"),
    bg="#2874f0",
    fg="white",
    padx=30,
    pady=10,
    bd=0,
    relief="flat",
    activebackground="#1558d6",
    command=organize_files
)
organize_btn.pack(pady=20)

# ------------------ RUN ------------------
window.mainloop()
