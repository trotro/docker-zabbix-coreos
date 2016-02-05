#!/bin/python

import socket
import httplib
import sys
import json

class UHTTPConnection(httplib.HTTPConnection):
    def __init__(self, path):
        httplib.HTTPConnection.__init__(self, 'localhost')
        self.path = path

    def connect(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(self.path)
        self.sock = sock

sock = UHTTPConnection("//coreos/var/run/docker.sock")
sock.request("GET", "/containers/json?all=0")
resRunning = sock.getresponse().read()
sock.request("GET", "/containers/json?all=1")
resAll = sock.getresponse().read()

runningContainers = len(json.loads(resRunning))
allContainers = len(json.loads(resAll))

print "%d/%d" % (runningContainers, allContainers) # print running/total
