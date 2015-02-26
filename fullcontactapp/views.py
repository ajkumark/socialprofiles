import ast
import requests
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext
from django.http import QueryDict
from django.core.exceptions import ObjectDoesNotExist

from fullcontactapp.models import Contact
from getcontactdetails.settings import FULLCONTACT_API_KEY

def home(request):
	if request.method == 'POST':
		email = request.POST['email']
		try:
			contact = Contact.objects.get(email=email)
			contact = contact.fullcontact_set.first()
			details = ast.literal_eval(contact.details)
		except ObjectDoesNotExist:
			payload = {'email':email, 'apiKey':FULLCONTACT_API_KEY }
			url = 'http://api.fullcontact.com/v2/person.json'
			r = requests.get(url, params=payload)
			if r.status_code == 200:
				contact = Contact.objects.create(email=email)
				contact.save()
				details = r.json()
				contact = contact.fullcontact_set.create(email=email, details=details)
				contact.save()
			else:
				print r.json()
				details = None
				return HttpResponse('not found')
		qdict = QueryDict('', mutable=True)
		qdict.update(details)
		return render_to_response('result.html', context_instance=RequestContext(request, {'data':qdict, 'email':contact.email}))
	else:
		return render_to_response('home.html', context_instance=RequestContext(request, {}))
