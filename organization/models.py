from django.db import models
from django.contrib.auth.models import User
import hashlib
import os
import time

def _createHash():
    """This function generate 10 character long hash"""
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return  hash.hexdigest()[:-10]

class Organization(models.Model):
	owner = models.ForeignKey(User)
	national_organization = models.CharField(max_length=500)
	chapter_name = models.CharField(max_length=500)
	join_token = models.CharField(max_length=10, default = _createHash, unique=True)


