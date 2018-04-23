# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 00:34:29 2018

@author: bmitra
"""

def hashing(s):
  h=7
  letters="acdegilmnoprstuw"
  for i in range(len(s)):
    h=h*37+letters.find(s[i])
  return h

def unhash(s):
  a=""
  letters="acdegilmnoprstuw"
  while s>7:
    a=letters[s%37]+a
    s=s//37
  return a

print(hashing("leepadg") )
print(unhash(930846109532517))

