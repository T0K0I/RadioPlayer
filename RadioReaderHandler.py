#!/home/basic/slushbin/slushbinenv/bin/python

#this creates the reading part of the pipe that later puts it to icecast
import subprocess


def startUpReader():
    print(subprocess.run(["ffmpeg -re -i radioInput.pipe -c:a libvorbis -q:a 1 -content_type application/ogg -f ogg icecast://source:password@localhost:8000/stream.ogg"],shell=True))
    startUpReader()
    
startUpReader()

