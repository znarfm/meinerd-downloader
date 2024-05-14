import customtkinter as ctk
from yt_dlp import YoutubeDL

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class MyFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = ctk.CTkLabel(self, text="MeiNerdDownloader", font=("Arial", 24))
        self.title.pack(pady=(0, 10))

        self.label_url = ctk.CTkLabel(self, text="Enter Youtube URL here:", font=("Arial", 16))
        self.label_url.pack(pady=(10, 0))

        self.entry_url = ctk.CTkEntry(self, placeholder_text="https://youtu.be/xxxxxxxxxx", width=250, height=40)
        self.entry_url.pack(pady=(10, 0))

        resolutions = self.btn_formats = ctk.CTkButton(self, text="Get Formats", height=40, command=self.get_formats)
        self.btn_formats.pack(pady=(10, 0))

        resolutions = ["720p", "480p", "360p", "240p", "144p"]
        self.combo_quality = ctk.CTkComboBox(self, values=resolutions, width=250, height=40)
        self.combo_quality.set("720p")
        self.combo_quality.pack(pady=(10, 0))

        self.btn_download = ctk.CTkButton(self, text="Download", height=40, command=self.download)
        self.btn_download.pack(pady=(10, 0))

        self.progress = ctk.CTkProgressBar(self)
        self.progress.set(0)
        self.progress.pack(pady=(10, 0))

        self.status = ctk.CTkLabel(self, text="Ready", font=("Arial", 16))
        self.status.pack(pady=(10, 0))

    def get_formats(self):
        try:
            ydl = YoutubeDL()
            info = ydl.extract_info(self.entry_url.get(), download=False)
            return info['formats']

        except Exception as e:
            print(f"Error: {e}")
            self.status.configure(text="Error: " + str(e))

    def download(self):
        # logging
        print(f"Quality: {self.combo_quality.get()}")
        print(f"Received URL: {self.entry_url.get()}")

        # reset status
        self.status.configure(text="Downloading...")
        self.progress.set(0)

        # download
        try:
            ydl_opts = {
                'format': f'bestvideo[height<={self.combo_quality.get()}]+bestaudio/best[height<={self.combo_quality.get()}]/best[height<={self.combo_quality.get()}]',
                'outtmpl': '%(title)s.%(ext)s',
                }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.entry_url.get()])
                

            # success
            self.status.configure(text="Download Complete")

        except Exception as e:
            print(f"Error: {e}")
            self.status.configure(text="Error: " + str(e))

        self.progress.set(100)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("MeiNerdDownloader")
        self.geometry("720x480")
        self.minsize(720, 480)

        self.frame = MyFrame(self)
        self.frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

app = App()


# spawn window
app.mainloop()