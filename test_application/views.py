# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore 
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.
def user(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			print 'logged in'
			login(request, user)
			return redirect('/app1/')
		# A backend authenticated the credentials

		else:
			sessionid=request.session.session_key
			return render(request,'test_application/user.html',{'sessionid':sessionid})
			# No backend authenticated the credentials
			sessionid=request.session.session_key
			print sessionid,request.session
			if username=="1":
				request.session.save()
				key=request.session.session_key
				print key
				Session.objects.get(pk=key).delete()
				
				request.session.create()
				sessionid=request.session.session_key
				print sessionid
	else:
		sessionid=None
	return render(request,'test_application/user.html',{'sessionid':sessionid})
	
	
	
	
def signin(request):
	s=request.session.create()
	sessionid=s.session_key
	session= Session.objects.get(pk=sessionid)
	
	
	
def signout(request):
	sessionid=request.session.session_key
	session= Session.objects.get(pk=sessionid)
	
	
	
	
	
	