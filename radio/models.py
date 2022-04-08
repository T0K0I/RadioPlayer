from django.core.validators import FileExtensionValidator
from django.utils import timezone

from django.db import models
from django.utils.timezone import now

class audioRequest(models.Model):
    name = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    find_on =  models.CharField(max_length=250)
    file = models.FileField(upload_to='static/radioFiles/ogg/', validators=[FileExtensionValidator(['ogg'])], null=True)
    isMusic = models.BooleanField(default=True)
    passedReview = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)


class messageRequest(models.Model):
    message = models.CharField(max_length=250)
    date_posted = models.DateTimeField(default=now)
    image = models.FileField(upload_to='static/radioFiles/img/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg', 'gif'])], null=True, blank=True)
    passedReview = models.BooleanField(default=False)


#used to know the last stored song and to retrieve it
class CurrentAudioHolder(models.Model):
    currentSong = models.ForeignKey(audioRequest, on_delete=models.SET_NULL, related_name='currentSong', null=True)
    nextSong = models.ForeignKey(audioRequest, on_delete=models.SET_NULL, related_name='nextSong', null=True)
    secondNextSong = models.ForeignKey(audioRequest, on_delete=models.SET_NULL, related_name='secondNextSong', null=True)

#used to know the last stored message and to retrieve it
class CurrentMessageHolder(models.Model):
    currentMessage = models.ForeignKey(messageRequest, on_delete=models.PROTECT)