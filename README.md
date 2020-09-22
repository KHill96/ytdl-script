# YouTube-DL Archive Script

### About
I made this script to automate the act of running the YouTube-DL command line tool. I changed it to run a multithreaded python script rather than a single terminal command with a batch file. I love the tool and wanted to automate and optimize the archiving process as much as I could.

### Breakdown
I originally got the majority of the command from [this post on reddit](https://www.reddit.com/r/DataHoarder/comments/c6fh4x/after_hoarding_over_50k_youtube_videos_here_is/) that showed a good way of downloading and archiving the videos downloaded. 

The full command that was being run was:
*youtube-dl.exe -i --geo-bypass --batch-file "list.txt" -f "(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best" --merge-output-format mkv --add-metadata -o "%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s" --download-archive "archive.txt" --yes-playlist --cookies "cookies.txt" --postprocessor-args "-id3v2_version 3"*

For most of the channels the options are the same as those above. The only exceptions are the UFC free fights and the ONE Championship playlist from Bleacher Report Live.

I created a different logger for each because i wanted to keep track of each channels status. The only thing that'll print are warnings and errors. The debug messages won't matter much to me as of right now.

Because of the different Loggers, there are also different options for each channel. The function that's place in each thread is the same with the arguments changing depending on the channel. I'm also going to set the time limit for each channel to be different since some of them. Other channels are just going to be removed sincce they don't upload any content anymore. HBO Boxing ended a few years ago so one pass over the channell will do.

I used the cookies.txt extension on chrome to get the cookie information needed for the script.

Any questions just hit me up.

KH
