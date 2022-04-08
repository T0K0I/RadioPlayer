import random
from radio.models import CurrentAudioHolder, CurrentMessageHolder, audioRequest, messageRequest


currentSongList = []


def updateHolder():
    Audioholder = CurrentAudioHolder.objects.get(id=2)

    Audioholder.currentSong = getRandomAudio()
    Audioholder.nextSong = getRandomAudio()
    Audioholder.secondNextSong = getRandomAudio()

    Audioholder.save()

def popOffSong():
    #get the holders
    print("popping off song")

    Audioholder = CurrentAudioHolder.objects.get(id=2)

    #move every song up
    Audioholder.currentSong = Audioholder.nextSong
    Audioholder.nextSong = Audioholder.secondNextSong
    #last one gets randomly picked from the list
    Audioholder.secondNextSong = getRandomAudio()

    #update the holders with a random song

    Audioholder.save()

    return Audioholder


def getRandomMessage():
    messagelist = list(messageRequest.objects.filter(passedReview=True))
    message = random.choice(messagelist)
    return message

def getRandomAudio():
    global currentSongList

    if(len(currentSongList) < 1):
        currentSongList = list(audioRequest.objects.filter(passedReview=True))

    #picks random index to not repeat songs
    index = random.randrange(len(currentSongList))
    currentSongList[index], currentSongList[-1] = currentSongList[-1], currentSongList[index]
    song = currentSongList.pop()
    #pops off the song 
    return song

#turn the id to 2 in production to not fuck up
def getCurrentPlaylist():
    Audioholder = CurrentAudioHolder.objects.get(id=2)

    return Audioholder

def getCurrentMessage():
    holder = CurrentMessageHolder.objects.get(id=1)
    message = holder.currentMessage
    return message
