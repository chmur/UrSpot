from django.db import models

class spots(models.Model):

	spotname = models.CharField(max_length = 50)
	authorname = models.Charfield(max_length = 50)
	link = models.URLField()
	description = models.Textfield
	// rating = models.DecimalField(max_value = 5, min_value = 1, max_digits = 1) 
	timestamp = models.DateTimeField()
