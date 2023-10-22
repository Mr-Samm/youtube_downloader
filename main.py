import yt_dlp
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import threading
import os

from tkinter import messagebox


class Downloader:
    def __init__(self, url, download_folder):
        self.url = url
        self.download_folder = download_folder

    def download(self):
        try:
            ydl_opts = {
                'outtmpl': os.path.join(self.download_folder, '%(title)s.%(ext)s'),
                'progress_hooks': [self.download_progress],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            messagebox.showinfo("Download Finished", "Download completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during the download:\n{str(e)}")

    def download_progress(self, data):
        if data['status'] == 'downloading':
            progress_value = data['_percent_str'].split('%')[0]
            download_speed = data['_speed_str']
            progress.set(progress_value)
            percentage_label.config(text=f"{data['_percent_str']} - {download_speed}")


save_location = os.path.expandvars(r'C:\Users\%username%\Downloads\Youtube_Downloader')
if not os.path.exists(save_location):
    os.mkdir(save_location)
else:
    pass


def location():
    global save_location
    save_location = filedialog.askdirectory()


def down_func():
    downloader = Downloader(entry.get(), save_location)
    if downloader:
        def cancel():
            if messagebox.askyesno(title="Cancel Download", message="Are you sure you want to Cancel the download?"):
                root.destroy()
                root.quit()
                exit()
            else:
                pass
        download_thread = threading.Thread(target=downloader.download)
        cancel = Button(250, 120, text="Cancel", command=cancel)
        download_thread.start()




class Button:
    def __init__(self, x, y, text, command):
        style = ttk.Style()
        self.width = 8
        style.configure("Cute.TButton",
                        background="pink",
                        foreground="black",
                        font=("Comic Sans MS", 8, "bold"),
                        relief="flat",
                        borderwidth=2,
                        width=self.width,
                        padding=4)
        self.button = ttk.Button(text=text, style="Cute.TButton", command=command, width=self.width)
        self.button.place(x=x, y=y)


root = tk.Tk()
root.minsize(width=480, height=200)
root.title("Youtube Downloader")
root.resizable(False, False)

progress = tk.StringVar()
progress_bar = ttk.Progressbar(root, mode='determinate', length=200, variable=progress)
progress_bar.place(x=90, y=90)

button = Button(160, 120, text="Download", command=down_func)
entry = tk.Entry(font=("Arial, 15"))
entry.place(x=90, y=50)
label = tk.Label(text="URL", font=("Arial, 15"))
label.place(x=30, y=50)
browse = Button(x=350, y=47, text="Browse", command=location)
browse.width = 1
percentage_label = tk.Label(root, text="", font=("Arial", 12))
percentage_label.place(x=300, y=90)

root.mainloop()
