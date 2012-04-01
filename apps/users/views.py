# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.utils import simplejson

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponse, Http404

def register_user(request):
    data = {}
    if request.user.is_authenticated():
        data['msg'] = 'USER_REGISTER_ERR_USER_LOGGED'
    elif request.POST and request.is_ajax():
        username = password = email = ''
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            data['msg'] = 'USER_REGISTER_OK'
        except Exception, e:
            data['msg'] = 'USER_REGISTER_ERR_USER_TAKEN'
    else:
        raise Http404
    return HttpResponse(
        simplejson.dumps(data),
        mimetype='application/json'
    )

def login_user(request):
    username = password = ''
    data = {}
    c = {}
    c.update(csrf(request))    
    if request.POST and request.is_ajax():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                data['user'] = username
                data['msg'] = 'USER_LOGIN_OK'
            else:
                data['msg'] = 'USER_LOGIN_ERR_NOT_ACTIVE'
        else:
            data['msg'] = 'USER_LOGIN_ERR_FAIL'
    else:
        raise Http404
    return HttpResponse(
        simplejson.dumps(data),
        mimetype='application/json'
    )

def logout_user(request):
    if request.POST and request.is_ajax():
        logout(request)
        data = {}
        data['msg'] = 'USER_LOGOUT_OK'
        return HttpResponse(
            simplejson.dumps(data),
            mimetype='application/json'
        )
    else:
        raise Http404

