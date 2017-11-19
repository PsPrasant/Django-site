# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib.auth import logout
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def view1(request):

	username = request.user.get_username()
	request.session['username']=username
	request.session.save()
	key= request.session['_auth_user_id']
	print key
	return render(request,'app001/user.html',{'username':username,'sessionid':request.session.session_key})
	
	
@login_required(login_url='/login/')	
def view_1(request):
	print request.user
	print request.user.is_authenticated()
	print request.user.get_username()
	the_username = request.user.get_username()
	key=User.objects.get(username=the_username).pk
	print key
	return render(request,'app001/user.html',{'username':the_username,'sessionid':request.session.session_key})
@login_required(login_url='/login/')
def view_2(request):
	print request.user
	print request.user.is_authenticated()
	print request.user.get_username()
	username = request.user.get_username()
	
	return render(request,'app001/user.html',{'username':username,'sessionid':request.session.session_key})
@login_required(login_url='/login/')
def view_3(request):
	print request.user
	print request.user.is_authenticated()
	print request.user.get_username()
	username = request.user.get_username()
	
	return render(request,'app001/user.html',{'username':username,'sessionid':request.session.session_key})	
@login_required(login_url='/login/')
def view_4(request):
	request.session.save()
	logout(request)
	username = request.user.get_username()
	return redirect('/login/')
	
