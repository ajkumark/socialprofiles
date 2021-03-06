import ast
import requests
import random
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template import RequestContext
from django.http import QueryDict
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from fullcontactapp.models import Contact, NotFoundContact, AprilFool, to_qdict, FullContact
from getcontactdetails.settings import FULLCONTACT_API_KEY, DUMMY_KEYS

import mandrill
MANDRILL_API_KEY = settings.EMAIL_HOST_PASSWORD
mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)

def call_fullcontact_api(email, FULLCONTACT_API_KEY):
	url = 'http://api.fullcontact.com/v2/person.json'
	payload = {'email':email, 'apiKey':FULLCONTACT_API_KEY }
	r = requests.get(url, params=payload)
	return r

def home(request):
	if request.method == 'POST':
		recaptcha =  request.POST.get('g-recaptcha-response')
		if recaptcha:
			email = request.POST['email']
			rejected_list = []
			try:
				contact = Contact.objects.get(email=email)
				contact = contact.fullcontact_set.first()
				details = ast.literal_eval(contact.details)
			except ObjectDoesNotExist:
				r = call_fullcontact_api(email,FULLCONTACT_API_KEY)
				if r.status_code == 403:
					rejected_list.append(FULLCONTACT_API_KEY)
					if len(rejected_list) == len(DUMMY_KEYS):
						print "return loop"
						msg = 'msg'
						return render_to_response('home.html', context_instance=RequestContext(request, {'msg':msg}))
					else:
						new_key = random.choice(filter(lambda x:x not in rejected_list, DUMMY_KEYS))
						print "new_key", new_key
						r =  call_fullcontact_api(email,new_key)
				if r.status_code == 200:
					contact = Contact.objects.create(email=email)
					contact.save()
					details = r.json()
					contact = contact.fullcontact_set.create(email=email, details=details)
					contact.save()
				else:
					try:
						notfound = NotFoundContact.objects.get(email=email)
						notfound.count += 1
						notfound.save()
					except ObjectDoesNotExist:
						notfound = NotFoundContact.objects.create(email=email)
						notfound.save()
					details = None
					msg = 'msg'
					return render_to_response('home.html', context_instance=RequestContext(request, {'msg':msg}))
			qdict = QueryDict('', mutable=True)
			qdict.update(details)
			return render_to_response('result.html', context_instance=RequestContext(request, {'data':qdict, 'email':contact.email}))
		else:
			msg = 'captcha'
			return render_to_response('home.html', context_instance=RequestContext(request, {'msg':msg}))
	else:
		msg = 'ssss'
		return render_to_response('home.html', context_instance=RequestContext(request, {}))

@login_required(login_url='/')
def view_profiles(request):
	full = FullContact.objects.values('details')
	output = map(to_qdict, full)
	return render_to_response('profiles.html', context_instance=RequestContext(request, {'data':output}))

def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		content = request.POST.get('description')
		print name,email,content
		content = 'Name: '+name+'\n'+'Email: '+email+'\n'+'Message: '+content
		try:
			message = {'from_email':'djangoajai@gmail.com',
					'subject': 'Socialprofiles',
					'to': [{'email': 'ajai.sreyas@gmail.com',
					'name': 'Ajai','type': 'to'}],
					'text': content,}
			result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
			msg = 'Thanks for the message, We will get back to you shortly...'
		except:
			msg = 'some error occured'
			pass
		return render_to_response('home.html', context_instance=RequestContext(request, {'msg':msg}))
	else:
		return render_to_response('contact.html', context_instance=RequestContext(request, {}))

def getmessages(request):
	if request.method == 'POST':
		try:
			phone = request.POST.get('phone')
			if len(phone) >=10:
				a = AprilFool.objects.create(phone=str(phone))
				a.save()
			msg = True
		except:
			msg = True
			pass
	else:
		msg = False
	return render_to_response('messages.html', context_instance=RequestContext(request, {'msg':msg}))

def test(request):
	return render_to_response('test.html', context_instance=RequestContext(request))
