from django.db import models

class Users(models.User):

    def __unicode__(self):
        return username
        