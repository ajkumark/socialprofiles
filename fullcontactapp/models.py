from django.db import models
from django.http import QueryDict
import ast

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


class NotFoundContact(models.Model):
	email = models.CharField(max_length=90, unique=True)
	count = models.IntegerField(default=1)

	def __unicode__(self):
		return str(self.email)

class AprilFool(models.Model):
	phone = models.CharField(max_length=90)

	def __unicode__(self):
		return str(self.phone)

def to_qdict(list_values):
	output = []
	qdict = QueryDict('', mutable=True)
	details = ast.literal_eval(list_values['details'])
	qdict.update(details)
	output.append(qdict)
	return output