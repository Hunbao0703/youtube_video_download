import os
import yt_dlp



def Download(url, height):
    ydl_opts = {
        'format': f'bestvideo[height<={height}]+bestaudio[ext=m4a]',  
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join("./video", '%(title)s_%(height)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Download is completed successfully")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    while True:
        quality = input("1. HD(720p)\n2. FHD(1080p defult)\n3. QHD(2k)\n4. UHD(4k)\nEnter Number: ")

        if quality == "1": height = 720
        elif quality == "3": height = 1440
        elif quality == "4": height = 2160
        else: height = 1080

        url = input("url: ")
        Download(url, height)

        check = input("done.\ncontinue?\n(Y/N):")

        if check.lower() == "y": continue
        else: break

    