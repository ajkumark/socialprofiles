from django.db import models

class Contact(models.Model):
	email = models.CharField(max_length=50, unique=True)
	# family_name
	# full_name
	# given_name
	# gender 
	# fb_url 
	# fb_username
	# tw_url 
	# tw_username

	def __unicode__(self):
		return str(self.email)



class FullContact(models.Model):
	email = models.ForeignKey(Contact, unique=True)
	details = models.TextField()

	def __unicode__(self):
		return str(self.email)