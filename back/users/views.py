# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.utils import simplejson

from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.http import HttpResponse, Http404


def login_user(request):
    username = password = ''
    data = {}
    c = {}
    c.update(csrf(request))    
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                data['status'] = 1
            else:
                data['status'] = 2
        else:
            data['status'] = 3
    else:
        raise Http404
    return HttpResponse(
        simplejson.dumps(data),
        content_type = 'application/json; charset=utf8'
    )

def logout_user(request):
    logout(request)
    data = {}
    data['status'] = 0
    return HttpResponse(
        simplejson.dumps(data),
        content_type = 'application/json; charset=utf8'
    )

