from django.shortcuts import render
from django.http import HttpResponseRedirect as red, HttpResponse as res
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from .models import Members

def testing(req):
  mydata = Members.objects.all().order_by('lastname', '-id').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata
  }
  return res(template.render(context, req))

def index(req):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers
  }
  return res(template.render(context, req))

def add(req):
  template = loader.get_template('add.html')
  return res(template.render({}, req))

def addrecord(req):
  x = req.POST['first']
  y = req.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return red(reverse('index'))

def delete(req, id):
  member = Members.objects.get(id=id)
  member.delete()
  return red(reverse('index'))

def update(req, id):
  mymember = Members.objects.get(id=id)
  template = template = loader.get_template('update.html')
  context = {
    'mymember': mymember
  }
  return res(template.render(context, req))

def updaterecord(req, id):
  first = req.POST['first']
  last = req.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return red(reverse('index'))