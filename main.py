import os
import time

def main():
    command = 'youtube-dl -i --geo-bypass --batch-file "list.txt" -f "(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best" --merge-output-format mp4 --add-metadata -o "%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s" --download-archive "archive.txt" --yes-playlist --cookies "cookies.txt" --postprocessor-args "-id3v2_version 3"'
    os.system(command)
    


if __name__ == "__main__":
    while True:
        main()
        time.sleep(1800)