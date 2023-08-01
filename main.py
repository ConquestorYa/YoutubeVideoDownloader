from pytube import YouTube
from rich.console import Console
import requests, climage
from os import system
import platform

console = Console()



def abort():
    console.print("[bold purple] \nAborting...")
    exit()

def get_thumbnail(thumbnail):
    img_data = requests.get(thumbnail).content
    with open('thumbnail.jpg', 'wb') as handler:
        handler.write(img_data)
    output = climage.convert('thumbnail.jpg')
    print(output)

banner = """
 █▀▄ ▄▀▄ █   █ █▄ █ █   ▄▀▄ ▄▀▄ █▀▄   ▀▄▀ ▄▀▄ █ █ ▀█▀ █ █ ██▄ ██▀   █ █ █ █▀▄ ██▀ ▄▀▄ ▄▀▀
 █▄▀ ▀▄▀ ▀▄▀▄▀ █ ▀█ █▄▄ ▀▄▀ █▀█ █▄▀    █  ▀▄▀ ▀▄█  █  ▀▄█ █▄█ █▄▄   ▀▄▀ █ █▄▀ █▄▄ ▀▄▀ ▄██
"""

while True: 
    console.print('[bold red]%s' % (banner,))
    try:

        user_input = input('\nPlease provide the YouTube video link for download. -> ')
        yt_video = YouTube(user_input)
        system('cls') if platform.system() == 'Windows' else system('clear')
        get_thumbnail(yt_video.thumbnail_url)
        console.print("[bold cyan]%s" % (yt_video.title,))
        video = yt_video.streams.get_highest_resolution()
        break
    except KeyboardInterrupt:
        abort()
    except:
        console.print('[bold red]Error: It seems the link provided is incorrect or broken.')
        console.print("[bold purple]Try Again")
        continue

try:  
    with console.status("[bold green]Downloading Video...") as status:
        video.download()
except KeyboardInterrupt:
    abort()

console.print('[bold green]Video Downloading is Completed!')
system('rm -rf thumbnail.jpg')







