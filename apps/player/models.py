import datetime

from django.db import models

"""Playlist Model -- Contains PlayListItems"""
"""class Playlist(models.Model):
    owner = models.ForeignKey('users.User')
    items = models.ManyToManyField('PlayListItem', related_name='playlists', blank=True, null=True)
    genre = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=datetime.datetime.now())"""


"""Playlist Items"""
"""class PlayListItem(models.Model):
    name = models.CharField(max_length=140)
    source = models.URLField(max_length=200)

    #Relations
    playlist = models.ForeignKey('Playlist', related_name='items', blank=True, null=True)
    
    def __unicode(self):
        return name"""