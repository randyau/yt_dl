# IPython log file
import pickle
import os
import random
import time
from pytube import Playlist
from pytube import YouTube

RECORD_FILE="record.pickle"
OUTDIR = "output/"

def prep_queue_record(queue):
    try:
        queue_record = pickle.load(open(RECORD_FILE,'rb'))
        print("record loaded")
    except Exception as e:
        print(e)
        print("creating new record")
        queue_record = {}

    for entry in queue:
        if entry in queue_record:
            pass
        else:
            queue_record[entry]=False#false because it's not downloaded
    return queue_record

def get_stream(url,stream_type='video'):
    """
    stream_type can be 'video' or 'audio'
    Returns stream object to call .download() on
    """
    if stream_type == 'video':
        return YouTube(url).streams.get_highest_resolution()
    elif stream_type == 'audio':
        return YouTube(url).streams.get_audio_only()
    else:
        return None

def download_all(queue_record, dl_type):
    "dl_type is passed straight to the stream getter, can be 'audio' or 'video'"
    for url,downloaded in queue_record.items():
        if downloaded:
            print("{}, cached".format(url))
            continue
        else:
            try:
                print("attempting: ", url)
                s_obj = get_stream(url,stream_type=dl_type)
                s_obj.download(output_path=OUTDIR)
                queue_record[url]=True #downloaded
                time.sleep(random.uniform(1,3))
                print("completed: ", url)
            except:
                print(url," failed")

def save_record(queue_record):
    pickle.dump(queue_record,open(RECORD_FILE,'wb'))

if __name__=="__main__":
    if not os.path.exists(OUTDIR):
        os.makedirs(OUTDIR)
    ifile = open("videos.txt",'r')
    queue = [x.strip() for x in ifile]
    dl_type = queue.pop(0) # the first line is a type indicator, video or audio
    queue_record = prep_queue_record(queue)
    download_all(queue_record, dl_type)
    save_record(queue_record)
