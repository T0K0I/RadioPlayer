#!/your/python/env
#important!
#for this to work, you need to make a fifo pipe called radioInput.pipe

import subprocess
import requests

def getUrl():
    return "http://yourUrl/popOff?format=json"


def streamCurrentSong(path):
    songname = path[1:len(path)]
    ffmpegProcess = subprocess.run(["ffmpeg -i " + songname + " -c:a libvorbis -q:a 1 -content_type application/ogg -f ogg pipe:1>radioInput.pipe"], shell=True)

def getNewSongPath():
    url = getUrl(False)
    PARAMS = {'pass':''}
    data = requests.get(url).json()
    currentSongPath = data['currentSong']['file']
    return currentSongPath
    # return data['file']

    #recursive functions which simply sends which song to play to ffmpeg
def startUpStreamer():
    songToPlay = getNewSongPath()

    #play a small audio file of silence for a more natural fading in
    ffmpegProcess = subprocess.run(["ffmpeg -i static/music/silenceBuffer.ogg -c:a libvorbis -q:a 1 -content_type application/ogg -f ogg pipe:1"], shell=True)

    streamCurrentSong(songToPlay)

    print("looped!")

    startUpStreamer()






startUpStreamer()