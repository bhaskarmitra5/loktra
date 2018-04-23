# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 12:09:48 2018

@author: bmitra


Created a Uri_util class which contains my all getter and setter methods.
We can extract all details from a uri link and can modify it.

Used regular expressions for extracting various components in URI.

The program runs a ininte loop until pressed 'c' when asked.


"""
import re

class uri_util:
  
  def __init__(self,uri):
    self.uri = uri
    self.scheme = "http"
    self.valid = True
    self.getDetails()
    
  def getScheme(self,uri):
    scheme=re.compile(r"^[a-z]+[:]\/\/")
    b=scheme.search(uri)
    try:
      return b.group()[0:-3],uri[b.end():]
    except:
      return self.scheme,uri
  
  def getDomain(self,uri):
    domain=re.compile(r"^[a-zA-Z0-9]+\-*[a-zA-Z0-9]+\.[a-z]+\.{0,1}[a-z]*")
    b=domain.search(uri)
    try:
      return b.group(),uri[b.end():]
    except:
      return ""
  
  def getPath(self,uri):
    path=re.compile(r"^\/[a-zA-Z0-9/]+")
    b=path.search(uri)
    try:
      return b.group()[1:],uri[b.end():]
    except:
      return "",uri
  
  def getQuery(self,uri):
    query=re.compile(r"^\?q=[a-zA-z0-9]+")
    b=query.search(uri)
    try:
      return b.group()[3:]
    except:
      return ""
    
  def getDetails(self):
    try:
      self.scheme,self.domain=self.getScheme(self.uri)
      self.domain,self.path = self.getDomain(self.domain)
      #print(self.domain,self.path)
      self.path,self.query=self.getPath(self.path)
      self.query=self.getQuery(self.query)
    except:
      #print()
      self.scheme = ""
      self.valid = False
      self.domain = ""
      self.path = ""
      self.query = ""
      
  def print(self):
    if self.valid:
      print("scheme : "+str(self.scheme))
      print("domain : "+str(self.domain))
      print("path : " + str(self.path))
      print("query : " + str(self.query))
    else:
      print("invalid uri")
      
  def changePath(self,newPath):
    try:
      _,_ = self.getPath(newPath)
      self.path=newPath
    except:
      print("invalid path entered")
      pass
  
  def changeQuery(self,newQuery):
    try:
      _= self.getQuery("?q="+newQuery)
      self.query=newQuery
    except:
      print("invalid Query entered")
      pass    
  
  def changeDomain(self,newDomain):
    try:
      _,_ = self.getDomain(newDomain+"://")
      self.domain=newDomain
    except:
      print("invalid domain entered")
      pass
  
  def changeScheme(self,newScheme):
    try:
      _,_ = self.getScheme(newScheme)
      self.scheme=newScheme
    except:
      print("invalid scheme entered")
      pass
    
  def displayUri(self):
    if self.valid:
      self.uri = self.scheme + "://" + self.domain + "/" + self.path
      if self.query != "":
        self.uri = self.uri + "?q=" + self.query
      print(self.uri)
    else:
      print("invalid uri,please modify uri")
    
u=uri_util("www.google.com/bhaskar?q=0")
u.print()

while True:
  i=input("select option: 1.change scheme, 2.change domain, 3.change path, 4.change query, c:to abort")
  if i=='1':
    a=input("enter scheme: ")
    u.changeScheme(a)
    
  if i=='2':
    a=input("enter domain: ")
    u.changeDomain(a)
    
  if i=='3':
    a=input("enter path: ")
    u.changePath(a)
    
  if i=='4':
    a=input("enter query: ")
    u.changeQuery(a)
    
  if i=='c':
    break
  else:
    print("invalid choice")
    continue
  
  print("modified uri: ")
  u.displayUri()