from download import *
from sessdata import *

if __name__ == "__main__":
    # Try to load sessdata from local file 
    sessdata = load_sessdata()
    # if the sessdata dont exist, get it from input
    if not sessdata:
        sessdata = input("Please input your sessdata:")
        # save the sessdata to local file 
        save_sessdata(sessdata)
    bvid = input("Please input your bvid:")
    download_video(bvid, sessdata)
