from rest_framework import serializers

from radio.models import messageRequest, audioRequest, CurrentAudioHolder


class audioSerializer(serializers.ModelSerializer):
    class Meta:
        model = audioRequest
        fields = ('name', 'artist', 'find_on', 'likes')

class filePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = audioRequest
        fields = ('file',)

class currentPlayingListSerializer(serializers.ModelSerializer):
    currentSong = audioSerializer()
    nextSong = audioSerializer()
    secondNextSong = audioSerializer()

    class Meta:
        model = CurrentAudioHolder
        fields = ('currentSong', 'nextSong', 'secondNextSong')



class currentPlayingListControlSerializer(serializers.ModelSerializer):
    currentSong = filePathSerializer()
    nextSong = filePathSerializer()
    secondNextSong = filePathSerializer()

    class Meta:
        model = CurrentAudioHolder
        fields = '__all__'



class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = messageRequest
        fields = ('message', 'image')