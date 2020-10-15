# YouTube-DL Archive Script

### About
I made this script to automate the act of running the YouTube-DL command line tool. I changed it to run a multithreaded python script rather than a single terminal command with a batch file. I love the tool and wanted to automate and optimize the archiving process as much as I could.

### Breakdown
I originally got the command from [this post on reddit](https://www.reddit.com/r/DataHoarder/comments/c6fh4x/after_hoarding_over_50k_youtube_videos_here_is/) that had shown a good way of downloading and archiving videos. 

The full command that was being run was:
*youtube-dl.exe -i --geo-bypass --batch-file "list.txt" -f "(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best" --merge-output-format mkv --add-metadata -o "%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s" --download-archive "archive.txt" --yes-playlist --cookies "cookies.txt" --postprocessor-args "-id3v2_version 3"*

In main.py, I had used the python library for youtube-dl to download the videos and channels concurrently using multiple threads. This worked out for some channels but not others. Partial downloads wouldn't resume and several videos would go ignored.
I had more success writing bash scripts using the command line arguments for youtube-dl and running those consecutively. I will look into running them indefinitely with different sleep timers for each script. 

I created scripts and lists for the different groups of channels (all appropriately named). 

Any questions just hit me up.

#### PS There's a bunch of errors for HBO Boxing because of the fact they privated so much of their content. And the UFC Espanol has some videos that don't download even though I have geo_bypass set to True. Might be an iusse with my understanding of it.

#### TODO: 
Add indefinite while loops to utilize the sleep function after the first run through on my machine.
