import sys
import csv
import time

from tqdm import trange
from pytube import YouTube

DOWNLOAD_FOLDER = './downloaded videos'

# Download function

def download(link):
    youtubeObject = YouTube(link)
    print(f"Donwloading: {youtubeObject.title}")
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(DOWNLOAD_FOLDER)
    except:
        print("An error has occurred")
        return False
    return True

def read_file(filename):
    data = []
    with open(filename, 'r') as f:
        file_contents = csv.reader(f)
        for line in file_contents:
            data.append(line[0])

    return data


def download_bulk(video_links):
    for link in trange(len(video_links)):
        download(video_links[link])


def main():
    if len(sys.argv) != 2:
        # Exit with error if no video link file is provided.
        print(f"Usage: python3 script.py video_links.csv")
        return

    else:
        # check for valid file
        filename = sys.argv[1]
        if not filename.endswith('.csv'):
            print("Please provide video links in csv format")
            return 

        # Load and read the video links

        video_links = read_file(filename)

        n_videos = len(video_links)
        print(f"Downloading {n_videos} Videos. ")

        # Donwload Videos
        download_bulk(video_links)


if __name__ == "__main__":
    main()