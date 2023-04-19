Quick youtube video/audio downloader

assumes list of links is in videos.txt
the first line **DMUST** have either **audio** or **video** in it to tell it what to download
one youtube video link per line

It is pretty braindead and grabs the 1st high quality stream (usually the best one) it's presented with.
Audio download will download audio-only mp4 files which you can extract using VLC

Files are saved in output/

It keeps a local pickle file (record.pickle) of past URLs it has successfully downloaded.
This lets you re-run the script to overcome the occasional error.

## Dependencies

Uses the most recent version of **pytube**, you might have to git clone 
https://github.com/nficano/pytube
and then link the pytube/ directory here if your version is not up to date with whatever is in pip
