import pytube
from tkinter import filedialog


async def get_save_path():
    return filedialog.asksaveasfilename(defaultextension=".*", filetypes=(('mp4', "*.mp4"),))


async def get_link(url):
    link = pytube.YouTube(url)
    return link


async def load(link: str, number_quality: str):
    
    path = await get_save_path()
    len_file_name = path[::-1].find('/')
    stream = link.streams.get_by_itag(number_quality)
    if len_file_name != -1:
        stream.download(path[:-len_file_name], path[len(path)-len_file_name:])

