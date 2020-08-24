from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def hello_world(req):
    return HttpResponse("Hello World!!")


def redirect_to_blog(req):
    return HttpResponseRedirect(reverse('blog:index'))


def to_test(req):
    return HttpResponse(" , ".join(dir(req)) + "<br>THIS IS TEST!!!<br><br>" + str(req.POST))
