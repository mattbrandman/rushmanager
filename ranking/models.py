from django.db import models
from jsonfield import JSONField

class Ranking(models.Model):
	ranking = JSONField()

