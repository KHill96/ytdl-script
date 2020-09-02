# YouTube-DL Archive Script

### About
I made this file to automate the act of running the YouTube-DL command line tool. Once every half hour it will run the command to download the channels and playlists listed in the file list.txt. I decided to do every half hour so that way I don't end up in any real trouble for making too many requests in such a short amount of time.

### Breakdown
I got the majority of the command from [this post on reddit](https://www.reddit.com/r/DataHoarder/comments/c6fh4x/after_hoarding_over_50k_youtube_videos_here_is/) that showed a good way of downloading and archiving the videos downloaded. A similar breakdown can be found there but since I tweaked the command a bit, I'll add one here as well.

The full command being run is:
*youtube-dl.exe -i --geo-bypass --batch-file "list.txt" -f "(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best" --merge-output-format mkv --add-metadata -o "%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s" --download-archive "archive.txt" --yes-playlist --cookies "cookies.txt" --postprocessor-args "-id3v2_version 3"*

I'll break it apart by the arguments which can be found here on the [YouTube-DL Github repository page](https://github.com/ytdl-org/youtube-dl/)

###### -i --geo-bypass
All this is doing is ignoring any errors, attempting to bypass any geological restrictions on the videos (which isn't too much of a concern for now).
###### --batch-file "list.txt"
This is the file containing all the channels and playlists that I want to archive. As time goes on I'll add more to the list.
###### -f "(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best"
This monstrosity of an argument is simply creating a priority of formats and encodings that I want to download. While it's pretty similar to the one found in the reddit post above, I added "[ext=mp4]" for all formats. This ensured that regardless of codec, I'll have an mp4 file. If an mp4 is somehow not available in 720 or 1080, then it'll just choose the best format according to the bitrate (the standard way YouTube-DL determines thet best format).
###### --merge-output-format mkv --add-metadata -o "%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s"
The merge-output-format is there to ensure that when the command is done merging the audio and video it holds the result in an mkv container. I wanted an mp4 container but the machine I'm running the script on was acting up so I settled on mkv. Again, pretty similar to the post linked above. I also add the metadata for each video and store the files using a folder structure of Playlist *Uploader/Playlist Title/ Title - Upload Date.extension*
###### --download-archive "archive.txt" --yes-playlist --cookies "cookies.txt" --postprocessor-args "-id3v2_version 3"
Finally, I tell the command to look to the file archive.txt to save time overwriting videos. I also give it the cookies file (since as of writing this I can't login through YouTube-DL without an error). I tell the command to treat every link as a playlist (since I do have only two links for playlists from one of the channels in list.txt).
I honestly have no clue how the postprocessor-args helps. I downloaded it to help embed thumbnails but there were issues with ffmpeg and the line just stuck.

###### PS I used the cookies.txt extension for chrome to download the cookies for the login info I'm using on YouTube.

That's my script. I've included the .py file to run it and the .txt file containing what channels and playlists I wanted to archive.

### TODO:
Multithreaded commands for each channel's playlists and uploads.
