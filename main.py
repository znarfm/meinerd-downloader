import customtkinter as ctk
from yt_dlp import YoutubeDL
import threading

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

        self.btn_formats = ctk.CTkButton(self, text="Get Formats", height=40, command=self.get_formats)
        self.btn_formats.pack(pady=(10, 0))

        self.radio_var = ctk.StringVar(value="video")
        self.radio_vid = ctk.CTkRadioButton(self, text="Video", variable=self.radio_var, value="video", command=self.update_format_selection)
        self.radio_vid.pack(pady=(10, 0))
        self.radio_audio = ctk.CTkRadioButton(self, text="Audio", variable=self.radio_var, value="audio", command=self.update_format_selection)
        self.radio_audio.pack(pady=(10, 0))

        self.label_resolution = ctk.CTkLabel(self, text="Select Resolution:", font=("Arial", 16))
        self.label_resolution.pack(pady=(10, 0))

        self.combo_quality = ctk.CTkComboBox(self, values=['Press get formats first'], width=250, height=40)
        self.combo_quality.pack(pady=(10, 0))

        self.btn_download = ctk.CTkButton(self, text="Download", height=40, command=self.start_download_thread)
        self.btn_download.pack(pady=(10, 0))

        self.progress = ctk.CTkProgressBar(self)
        self.progress.set(0)
        self.progress.pack(pady=(10, 0))

        self.status = ctk.CTkLabel(self, text="Ready", font=("Arial", 16))
        self.status.pack(pady=(10, 0))

    def update_format_selection(self):
        if self.radio_var.get() == "audio":
            self.label_resolution.configure(state="disabled")
            self.combo_quality.configure(state="disabled")
        else:
            self.label_resolution.configure(state="normal")
            self.combo_quality.configure(state="normal")

    def start_download_thread(self):
        url = self.entry_url.get()
        resolution = self.combo_quality.get()

    def get_formats(self):
        self.status.configure(text="Fetching formats...")
        url = self.entry_url.get()

        def fetch_formats():
            ydl_opts = {
            'listformats': True,
            'quiet': True
            }
            try:
                with YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(url, download=False)
                    formats = info_dict['formats']

                    if self.radio_var.get() == "audio":
                        resolutions = sorted(set(f['format_note'] for f in formats if 'format_note' in f and 'audio' in f['format_id']))
                    else:
                        resolutions = sorted(set(f['format_note'] for f in formats if 'format_note' in f and 'video' not in f['format_id']))

                    self.combo_quality.configure(values=resolutions)
                    self.combo_quality.set(resolutions[0] if resolutions else 'No formats found')
                    self.status.configure(text="Formats fetched")

            except Exception as e:
                print(f"Error: {e}")
                self.status.configure(text="Error: " + str(e))
            
        threading.Thread(target=fetch_formats).start()

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            downloaded = d.get("downloaded_bytes", 0)
            total = d.get("total_bytes", 1)
            progress = downloaded / total
            self.progress.set(progress)
            self.status.configure(text="Downloading...")

        elif d['status'] == 'finished':
            self.progress.set(100)
            self.status.configure(text="Download Complete")

    def download(self):
        format = self.radio_var.get()
        quality = self.combo_quality.get()
        url = self.entry_url.get()
        
        # logging
        print(f"Format: {format}")
        print(f"Quality: {quality}")
        print(f"Received URL: {url}")

        # reset status
        self.status.configure(text="Downloading...")
        self.progress.set(0)

        # download
        try:
            if format == "audio":
                ydl_opts = {
                'format': 'bestaudio[ext=mp3]/bestaudio',
                'outtmpl': '%(title)s-%(abr)sk.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'progress_hooks': [self.progress_hook]
                }

            else:
                ydl_opts = {
                'format': f'best[height<={quality[:-1]}][ext=mp4]/bestaudio[ext=m4a]',
                'outtmpl': '%(title)s-%(resolution)s.%(ext)s',
                'progress_hooks': [self.progress_hook]
                }
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.entry_url.get()])
                

            # success
            self.status.configure(text="Download Complete")

        except Exception as e:
            print(f"Error: {e}")
            self.status.configure(text="Error: " + str(e))

    def start_download_thread(self):
        dl_thread = threading.Thread(target=self.download)
        dl_thread.start()

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