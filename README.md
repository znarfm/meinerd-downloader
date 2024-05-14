# MeiNerdDownloader

## IMPORTANT

⚠️ Project is still in development. Lot's of bugs ahead. ⚠️
I only do this during my free time and to explore GUI stuff. 

## Description

MeiNerdDownloader is a simple graphical user interface (GUI) wrapper for yt-dlp, designed to make downloading videos and audio from YouTube as straightforward as possible. Built with customtkinter, it offers a more modern look from the usual tkinter. This simple project aims to make the process of fetching and downloading media from YouTube accessible to everyone.

## Features

- **Easy-to-use Interface**: A clean and intuitive GUI for all user levels.
- **Video and Audio Download**: Supports downloading both video and audio formats.

## Installation

To use this program, you need to have Python installed on your system. Clone the repo and install the required dependencies:

```bash
git clone https://github.com/znarfm/meinerd-downloader/
cd meinerd-downloader
pip install -r requirements.txt
```

## Usage

Run the application by executing the following command in the terminal:

```bash
python main.py
```

Once the app is running:

1. Enter the YouTube URL in the input field.
2. Click 'Get Formats' to fetch the available formats.
3. Choose 'Video' or 'Audio' and select the desired resolution from the dropdown menu.
4. Click 'Download' to start the download process.

## Dependencies

- yt-dlp: for downloading videos and audio
- customtkinter: for creating the GUI

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pr.

## Acknowledgements

- Thanks to the developers of [yt-dlp](https://github.com/yt-dlp/yt-dlp) for their fantastic command-line tool.
- Thanks to [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for providing an easy-to-use tool to build a modern GUI in Python.

## To-do's

- Fix resolution filtering system.
- Fix video download not respecting the resolution picked in the combobox.
- Add thumbnail to audio downloads.
- Add option to enable cc downloads for videos.
- Add option to set a custom path for output files.
- Add label to show path and filename of output files.
- Add button to open file manager to select output path.
- Provide builds using PyInstaller.
- Fix my lazy ass.
