# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',

    url(r'^$', 'home.views.index', name='index'),

    # 404 y 500 errors
    url(r'^404$',  direct_to_template, {'template': '404.html'}),
    url(r'^500$',  direct_to_template, {'template': '500.html'}),

)