from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class spots(models.Model):

	spotname = models.CharField(max_length = 30)
	authorname = models.CharField(max_length = 20)
	link = models.URLField()
	description = models.TextField()
	#rating = models.DecimalField(max_digits = 1, decimal_places = 1) # max_value = 5.0, min_value = 1.0)
	timestamp = models.DateTimeField(default=timezone.now) 
	tags = TaggableManager()
#	published_date = models.DateTimeField(blank=True, null=True)

#def publish(self):
#    self.published_date = timezone.now()
#    self.save()

#def __str__(self):
#    return self.title

def __unicode__(self):
	return self.spotname
