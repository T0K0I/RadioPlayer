from django.urls import path

from . import views
from django.urls import include, path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('currentsong', views.get_current_song),
    path('', views.index, name='slushbin'),
    path('radio', views.radio, name='radio'),

    path('uploadMessage', views.uploadMessage, name='upload'),
    path('uploadAudio', views.uploadSong, name='upload'),

    path('actionCompleted', views.messageResponse, name='action completed'),


    #api calls
    path('currentSong', views.getCurrentSong, name='song'),
    path('currentMessage', views.getCurrentMessage, name='message'),

    #admin stuff
    path('initH', views.initHolders),
    path('popOff', views.popOff),

    path('listAll', views.showAllFiles, name='links'),

    path('passMessage/<int:id_to_use>', views.passMessage),
    path('deleteMessage/<int:id_to_use>', views.deleteMessage),
    path('passAudio/<int:id_to_use>', views.passAudio),
    path('deleteAudio/<int:id_to_use>', views.deleteAudio),

]




