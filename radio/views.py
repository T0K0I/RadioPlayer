from random import shuffle

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ipware import get_client_ip
from rest_framework.decorators import api_view
from rest_framework.response import Response
from radio.customScripts import radioRequestHandler
from radio.customScripts.forms import MessageUploadForm, audioUploadForm
from . import models
from .customScripts.radioRequestHandler import popOffSong
from .customScripts.serializers import messageSerializer, currentPlayingListSerializer, \
    currentPlayingListControlSerializer


def index(request):
    return render(request, 'radio/main.html')

def radio(request):
    return render(request, 'radio/radio.html')

def uploadMessage(request):
    if request.method == 'POST':

        # form that is used
        messageForm = MessageUploadForm(request.POST, request.FILES)
        print(request.POST)
        if (messageForm.is_valid()):
            messageForm.save()
            print("passed")
            return HttpResponseRedirect('/actionCompleted')

    else:
        messageForm = MessageUploadForm()

    context = {
        'form': messageForm
    }

    return render(request, 'radio/upload.html', context)

def uploadSong(request):
    if request.method == 'POST':
        if check_admin(request):
            # form that is used
            messageForm = audioUploadForm(request.POST, request.FILES)
            if (messageForm.is_valid()):
                messageForm.save()
                return HttpResponseRedirect('/actionCompleted')

    else:
        messageForm = audioUploadForm()

    context = {
        'form': messageForm
    }

    return render(request, 'radio/upload.html', context)


def messageResponse(request):
    return render(request, 'radio/message.html')

def initHolders(request):
    if check_admin(request):
        radioRequestHandler.updateHolder()
        return None

def showAllFiles(request):
    if check_admin(request):
        #messages
        passedMessages = models.messageRequest.objects.filter(passedReview = True)
        unpassedMessages = models.messageRequest.objects.filter(passedReview = False)
        #sounds
        passedAudio = models.audioRequest.objects.filter(passedReview = True)
        unpassedAudio = models.audioRequest.objects.filter(passedReview = False)

        for i in unpassedAudio:
            print(i.passedReview)

        context = {
            'passedMessages': passedMessages,
            'unpassedMessages': unpassedMessages,
            'passedAudio': passedAudio,
            'unpassedAudio': unpassedAudio,
        }
        return render(request, 'radio/uploadList.html', context)
    return None

def deleteMessage(request, id_to_use):
    if check_admin(request):
        toDelete = models.messageRequest.objects.filter(id = id_to_use)
        toDelete.delete()
        return HttpResponseRedirect('/listAll')

def passMessage(request, id_to_use):
    if check_admin(request):
        toPass = models.messageRequest.objects.filter(id = id_to_use).update(passedReview = True)
        return HttpResponseRedirect('/listAll')

def deleteAudio(request, id_to_use):
    if check_admin(request):
        toDelete = models.audioRequest.objects.get(id = id_to_use)
        toDelete.delete()
        return HttpResponseRedirect('/listAll')

def passAudio(request, id_to_use):
    if check_admin(request):
        toPass = models.audioRequest.objects.filter(id = id_to_use).update(passedReview = True)
        return HttpResponseRedirect('/listAll')

# api calls

@api_view(['GET'])
def getCurrentSong(request):
    holder = radioRequestHandler.getCurrentPlaylist()
    serializer = currentPlayingListSerializer(holder)
    return Response(serializer.data)

@api_view(['GET'])
def popOff(request):
    holder = radioRequestHandler.popOffSong()
    serializer = currentPlayingListControlSerializer(holder)
    return Response(serializer.data)

@api_view(['GET'])
def getCurrentMessage(request):
    msgReq = radioRequestHandler.getRandomMessage()
    serializer = messageSerializer(msgReq)
    return Response(serializer.data)

#misc
def check_admin(request):
    return True
